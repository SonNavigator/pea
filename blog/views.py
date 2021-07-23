from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm
from django.db.models import Q


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


def contact(request):
    # Check an incoming request
    # And a form sent by client should be POST method
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # If not POST method, display blank form
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})


def search(request):
    # Get an incoming query string sent by client
    search_post = request.GET.get('q')
    if search_post:
        # Query data from the database if matched
        post = Post.objects.filter(Q(title__contains=search_post))
    else:
        # Redirect to homepage
        return redirect('/')

    return render(request, 'blog/search.html', {'post': post})
