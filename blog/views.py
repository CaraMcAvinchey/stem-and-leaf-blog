from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Plant
from .forms import CommentForm


class PlantList(generic.ListView):
    model = Plant
    queryset = Plant.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PlantDetail(View):

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
