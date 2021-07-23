from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm
from django.db.models import Q


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
    val = 20
    val2 = 30
    return render(request, 'blog/about.html', {'val': val, 'val2': val2})


def contact(request):
    # form = ContactForm()
    if request.method == "POST":
        # print("Okay POST")
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # print("Not POST")
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})


def search(request):
    search_post = request.GET.get('q')
    if search_post:
        # print("Client sends: ", search_post)
        post = Post.objects.filter(Q(title__contains=search_post))
    else:
        return redirect('/')

    return render(request, 'blog/search.html', {'post': post})
