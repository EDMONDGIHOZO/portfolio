from django.shortcuts import render
from blog.models import Post, Comment, Category
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}

    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )

    context = {"category": category, "posts": posts}

    return render(request, "category.html", context)


def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_details.html", context)
