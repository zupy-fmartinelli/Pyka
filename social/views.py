from django.shortcuts import render
from django.views import View
from .models import Post


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by("-create_on")
        return render(request, "social/post_list.html", {"posts": posts})

        context = {
            'post_list': posts,
        }

        return render(request, 'social/post_list.html', context)
