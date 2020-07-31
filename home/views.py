from django.shortcuts import render, redirect
from random import random
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Contact
from django.contrib import messages
from blog.models import Post


# Create your views here.

def home(request):
    allPosts = Post.objects.all()[:4]
    #allPosts = Post.objects.order_by('?')[0]
    context = {'allPosts': allPosts}
    #jac = sample(allPosts(), 2)
    return render(request, 'home/home.html', context)
    #return HttpResponse("this is home")


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'please fill form correctly.')
        else:
            content = Contact(name=name, email=email, phone=phone, content=content)
            content.save()
            messages.success(request, 'Your message has been successfuly send.')
    return render(request, 'home/contact.html')
    #return HttpResponse("contact us")


def about(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/about.html', context)
    #return HttpResponse("about us")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    #allPosts = Post.objects.all()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, 'No Search Results Found. Please refine your query.')
    else:
        messages.success(request, 'Search Results Found. Please find your query.')

    params ={'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html', params)
    #return HttpResponse("search context")

def handleSignup(request):
    if request.method == 'POST':
        #get the post parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for erroneous input
        # check for username should be under 10 character
        if len(username) > 10:
            messages.error(request, "Username must beunder 15 character")
            return redirect('home')

        # check for username should be in alphabet and numric
        if not username.isalnum():
            messages.error(request, "Username must be requred alphabets and numbers")
            return redirect('home')

        # check for password1 and password2 match
        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')

        #check for password shold be max 8 char
        if len(pass1) < 8:
            messages.error(request, "Password should be required max 8 character")
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exist")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exist")
            return redirect('home')



        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your icoder account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 -- Not Found")

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername ,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('home')

    return HttpResponse("404 -- Not Found")


def handlelogout(request):
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect('home')