from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.template.context_processors import csrf
from django.utils import timezone
from django.views.generic import UpdateView
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from blog.forms import PostForm
from home.forms import ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from plotly.offline import plot
from plotly.graph_objs import Scatter

#login form  ----------------------------------------------------------------------------

def admslogin(request):
    if request.method == 'POST':
        admsUsername = request.POST['admsUsername']
        admsPassword = request.POST['admsPassword']

        user = authenticate(username=admsUsername ,password=admsPassword)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect('admsblog')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('admslogin')

    return render(request, 'adms/admslogin.html')


# logout -----------------------------------------------------------------------------

@permission_required('is_superuser')
def admslogout(request):
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect('admslogin')


# contact details --------------------------------------------------------------------------

@permission_required('is_superuser')
def admscontact(request):
    allcontact = Contact.objects.all()
    context = {'allcontact': allcontact}
    return render(request, 'adms/admscontact.html', context)

@permission_required('is_superuser')
# add contact
def addcontact(request):
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
    return render(request, 'adms/addcontact.html')

@permission_required('is_superuser')
# delete blog
def contactdelete(request, sno):
    allcontact = Contact.objects.get(sno=sno)
    allcontact.delete()
    messages.success(request, "You successfully Deleted the post")
    return redirect("admscontact")

def contactsearch(request):
    query = request.GET['query']
    if len(query) > 78:
        allcontact = Contact.objects.none()
    # allPosts = Post.objects.all()
    else:
        allcontactname = Contact.objects.filter(name__icontains=query)
        allcontactsno = Contact.objects.filter(sno__icontains=query)
        allcontact = allcontactname.union(allcontactsno)

    if allcontact.count() == 0:
        messages.warning(request, 'No Search Results Found. Please refine your query.')
    else:
        messages.success(request, 'Search Results Found. Please find your query.')

    params = {'allcontact': allcontact, 'query': query}
    return render(request, 'adms/admscontact.html', params)




# Blog Details ---------------------------------------------------------------------

@permission_required('is_superuser')
def admsblog(request):
    if request.user.is_superuser:
        allPosts = Post.objects.all()
        context = {'allPosts': allPosts}
    else:
        return redirect('home')
    return render(request, 'adms/admsblog.html', context)




@permission_required('is_superuser')
# add blog
def uploadblog(request):
    upload = PostForm()
    if request.method == 'POST':
        upload = PostForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('admsblog')
        else:
            return HttpResponse("""your form is wrong, reload on """)
    else:
        return render(request, 'adms/uploadblog.html', {'upload':upload})

@permission_required('is_superuser')
# edit blog
def blogedit(request, sno):
    post = get_object_or_404(Post, sno=sno)
    post_form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if post_form.is_valid():
        edit = post_form.save(commit=False)
        edit.save()
        return redirect('admsblog')
    return render(request, 'adms/blogedit.html', {'post_form': post_form})


@permission_required('is_superuser')
# delete blog
def blogdelete(request, sno):
    allPosts = Post.objects.get(sno=sno)
    allPosts.delete()
    messages.success(request, "You successfully Deleted the post")
    return redirect("admsblog")

def blogsearch(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    # allPosts = Post.objects.all()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostssno = Post.objects.filter(sno__icontains=query)
        allPosts = allPostsTitle.union(allPostssno)

    if allPosts.count() == 0:
        messages.warning(request, 'No Search Results Found. Please refine your query.')
    else:
        messages.success(request, 'Search Results Found. Please find your query.')

    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'adms/admsblog.html', params)
    #return HttpResponse("search context")

# USER details ---------------------------------------------------------------

@permission_required('is_superuser')
def admsuser(request):
    allusers = User.objects.filter(is_superuser=0)
    #allusers = User.objects.filter(is_superuser= 0)
    context = {'allusers': allusers}
    return render(request, 'adms/admsuser.html', context)

@permission_required('is_superuser')
# delete blog
def userdelete(request, id):
    allusers = User.objects.get(id=id)
    allusers.delete()
    #context = {'user': user}
    messages.success(request, "You successfully Deleted the user")
    return redirect("admsuser")

def usersearch(request):
    query = request.GET['query']
    if len(query)>78:
        allusers = User.objects.none()
    #allPosts = Post.objects.all()
    else:
        allusersusername = User.objects.filter(username__icontains=query, is_superuser=0)
        allusersid = User.objects.filter(id__icontains=query, is_superuser=0)
        allusers = allusersusername.union(allusersid)

    if allusers.count() == 0:
        messages.warning(request, 'No Search Results Found. Please refine your query.')
    else:
        messages.success(request, 'Search Results Found. Please find your query.')

    params ={'allusers': allusers, 'query':query}
    return render(request, 'adms/admsuser.html', params)
    #return HttpResponse("search context")




# edit blog-------------------------------------------------------------------------------------
#@permission_required('is_superuser')
#def blogedit(request, sno):
#    obj = get_object_or_404(Post, sno=sno)
#
 #   form = PostForm(request.POST or None, instance=obj)
 #   context = {'form': form}

  #  if form.is_valid():
   #     obj = form.save(commit=False)

#        obj.save()

 #       messages.success(request, "You successfully updated the post")

   #     context = {'form': form}

  #      return render(request, 'adms/blogedit.html', context)

 #   else:
  #      context = {'form': form}
  #      messages.warning(request, "You can edit blog hear")
  #      return render(request, 'adms/blogedit.html', context)




def pie_chart(request):
    x_data = [0, 1, 2, 3]
    y_data = [x ** 2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div')

    return render(request, 'adms/pie_chart.html', context={'plot_div': plot_div})


def dump(request):
    """
    Downloads all movies as Excel file with a single worksheet
    """
    post_queryset = Post.objects.all()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',)
    response['Content-Disposition'] = 'attachment; filename={date}-movies.xlsx'.format(date=timeStamp.now().strftime('%Y-%m-%d'),)
    Postform = PostForm()

    # Get active worksheet/tab
    worksheet = PostForm.active
    worksheet.title = 'Blog Details'

    # Define the titles for columns
    columns = ['sno', 'Title', 'content', 'author', 'slug', 'timeStamp',]
    row_num = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    # Iterate through all movies
    for post in post_queryset:
        row_num += 1

        # Define the data for each cell in the row
        row = [post.sno, post.title, post.content, post.author, post.slug, post.timeStamp, ]

        # Assign the data for each cell of the row
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    Postform.save(response)


    return response


# Blog Details ---------------------------------------------------------------------


def admsblog2(request):

    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'adms/demoblogsearch.html', context)


def admsblogview(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'adms/view.html', context)
'''
def blogsearch2(request):
    query = request.GET['query']
    allPostssno = Post.objects.filter(sno__icontains=query)
    allusers = allPostssno
    if allusers.count() == 0:
        messages.warning(request, 'No Search Results Found. Please refine your query.')
    else:
        messages.success(request, 'Search Results Found. Please find your query.')
    params = {'allusers': allusers, 'query':query}
    return render(request, 'adms/demoblogsearch.html', params)
    #return HttpResponse("search context")
    '''

def blogsearch2(request, template_name='adms/demoblogsearch.html'):

    if request.GET.get('featured'):
        featured_filter = request.GET.get('featured')
        listings = Post.objects.filter(sno=featured_filter)
    else:
        listings = Post.objects.all()

    context_dict = {'listings': listings}
    return render(request, template_name, context_dict)

def blogedit2(request, sno):
    post = Post.objects.filter(sno=sno).first()
    #post = get_object_or_404(Post, sno=sno)
    post_form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if post_form.is_valid():
        edit = post_form.save(commit=False)
        edit.save()
        return redirect('admsblog2')
    return render(request, 'adms/blogedit2.html', {'post_form': post_form, 'post':post})







