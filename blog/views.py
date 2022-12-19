from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Plant
from .forms import CommentForm

from django.contrib.messages.views import SuccessMessageMixin


class PlantList(generic.ListView):
    model = Plant
    queryset = Plant.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PlantDetail(SuccessMessageMixin, View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Plant.objects.filter(status=1)
        plant = get_object_or_404(queryset, slug=slug)
        comments = plant.comments.filter(approved=True).order_by('created_on')
        liked = False
        if plant.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "plant": plant,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Plant.objects.filter(status=1)
        plant = get_object_or_404(queryset, slug=slug)
        comments = plant.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if plant.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = plant
            comment.save()
            messages.success(request,
                             'Your comment has been uploaded successfully.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "plant": plant,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Plant, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
