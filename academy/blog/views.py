from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.


def post_list(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f"post list archive for {year} and {month}")

    if year is not None:
        return HttpResponse(f"post list archive for {year}")
    return HttpResponse("<h1>H1 tag</h1><br><h2>H2 tag</h2>")


class BlogPostList(ListView):
    model = Post


def categories_list(request):
    return HttpResponse("category list page")


def post_detail(request, post_slug):
    return HttpResponse(f"post detail {post_slug}")


class BlogPostDetailView(DetailView):
    model = Post


def custom_post_detail(request):
    return HttpResponse("custom post detail")


