from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from .models import Author, Post, Tag
from django.views.generic import View, ListView, CreateView, FormView, DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect


def get_date(post):
    post = Post.objects.all()
    return post


class StartingPostView(ListView):
    template_name = "blog/index.html"
    model = Post
    paginate_by = 3
    ordering = ["-date"]
    context_object_name = "posts"


class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = Post.objects.get(slug=slug)
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "tags": post.tags.all(),
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False

        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")
