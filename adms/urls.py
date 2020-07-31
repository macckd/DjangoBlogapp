"""icoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from. import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.admslogin, name='admslogin'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='adms/change-password.html',success_url='/adms/admsblog'), name='change_password'),
    path('admslogout', views.admslogout, name='admslogout'),
    path('admscontact', views.admscontact, name='admscontact'),
    path('admsblog', views.admsblog, name='admsblog'),
    path('admsblogview/<str:slug>', views.admsblogview, name='admsblogview'),
    path('admsuser', views.admsuser, name='admsuser'),
    path('usersearch', views.usersearch, name='usersearch'),
    path('blogsearch', views.blogsearch, name='blogsearch'),
    path('contactsearch', views.contactsearch, name='contactsearch'),
    path('userdelete/<int:id>', views.userdelete, name='userdelete'),
    path('blogedit/<int:sno>', views.blogedit, name='blogedit'),
    path('uploadblog', views.uploadblog, name='uploadblog'),
    path('blogdelete/<int:sno>', views.blogdelete, name='blogdelete'),
    path('addcontact', views.addcontact, name='addcontact'),
    path('contactdelete/<int:sno>', views.contactdelete, name='contactdelete'),
    path('pie_chart', views.pie_chart, name='pie_chart'),
    path('dump', views.dump, name='dump'),
    path('admsblog2', views.admsblog2, name='admsblog2'),
    path('blogsearch2', views.blogsearch2, name='blogsearch2'),
    path('blogedit2/<int:sno>', views.blogedit2, name='blogedit2'),
    #path('post_new', views.post_new, name='post_new')

    #path('contact', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
