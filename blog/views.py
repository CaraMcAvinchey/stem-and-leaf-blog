from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Plant, Comment
from .forms import CommentForm, EditForm

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
                             'Your comment has been uploaded for approval.')
            comment_form = CommentForm()
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


class PostLike(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Plant, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    If user is logged in:
    Direct user to delete_comment.html template
    User will be prompted with a message to confirm deletion.
    """
    model = Comment
    template_name = "delete_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def delete(self, request, *args, **kwargs):
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        PlantDetail.comment_deleted = True
        messages.success(self.request, 'Your comment has been deleted.')
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})


class CommentEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    If user is logged in:
    Direct user to update_comment.html template,
    displaying ReviewForm for that specific review.
    Post edited info back to the database and return user to post.
    """
    model = Comment
    form_class = EditForm
    template_name = "edit_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def form_valid(self, form):
        """
        Upon success prompt the user with a success message.
        """
        super().form_valid(form)
        messages.success(self.request, 'Your comment has been edited.')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        """
        Upon success returns user to the post detail page.
        """
        PlantDetail.comment_edited = True
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})


class Page403(TemplateView):
    template_name = '403.html'


class Page404(TemplateView):
    template_name = '404.html'


class Page500(TemplateView):
    template_name = '500.html'
