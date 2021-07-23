from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    # Get all posts
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': all_posts})


def post_detail(request, id):
    # Get only one post
    single_post = Post.objects.get(pk=id)
    return render(request, 'blog/post-detail.html', {'post': single_post})


def about(request):
    return render(request, 'blog/about.html')
