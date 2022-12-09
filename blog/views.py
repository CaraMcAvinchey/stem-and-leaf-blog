from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Plant


class PlantList(generic.ListView):
    model = Plant
    queryset = Plant.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PlantDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Plant.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked
            },
        )
