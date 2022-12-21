from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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

# comments delete and edit functions


@method_decorator(login_required, name="dispatch")
class CommentDelete(DeleteView):
    """
    If user is logged in:
    Direct user to delete_comment.html template
    User will be prompted with a message to confirm.
    """
    model = Comment
    template_name = "delete_comment.html"

    def delete(self, request, *args, **kwargs):
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        PlantDetail.comment_deleted = True
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})


@method_decorator(login_required, name="dispatch")
class CommentEdit(UpdateView):
    """
    If user is logged in:
    Direct user to update_comment.html template,
    displaying ReviewForm for that specific review.
    Post edited info back to the DB and return user to post.
    """
    model = Comment
    form_class = EditForm
    template_name = "edit_comment.html"

    def form_valid(self, form):
        """
        Upon success prompt the user with a success message.
        """
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        """
        Upon success returns user to the stock detail page.
        """
        PlantDetail.comment_edited = True
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})
