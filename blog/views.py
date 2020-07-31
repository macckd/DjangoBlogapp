from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse

from blog.forms import PostForm
from blog.models import Post



# Create your views here.
from home.models import Contact


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)
    #return HttpResponse("hello blogHome")


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    allPosts = Post.objects.all()
    context = {'post': post, 'allPosts': allPosts}
    return render(request, 'blog/blogPost.html', context)
    #return HttpResponse(f'hello blogHop: {slug}')

def uploadblog1(request):
    upload = Post.objects.all()
    print(upload)
    return render(request, 'blog/cb.html', {'upload':upload})

