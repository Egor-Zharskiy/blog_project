from django.shortcuts import render, HttpResponse

from posts.models import Post, Category


def index(request, category_id=None):
    posts = Post.objects.filter(category_id=category_id) if category_id else Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, "index.html", context)


def article(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, "article.html", context)
