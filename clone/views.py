from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Profile,User,Image
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from .forms import *


# Create your views here.
def welcome(request):
    '''
    Function to display the index page
    '''
    user = request.user
    all_images = []
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
    else:
        form = ImageForm()

    try:
        images = Image.objects.all()
    except Image.DoesNotExist:
        images = None
    return render(request ,'index.html' , { 'images': images , 'form': form})


def signup(request):
    '''
    Function to return the signup page
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request , 'registration/signup.html', {
        "form":form
    })

def profile(request):
    '''
    Function to return the profile page
    '''
    user = request.user
    all_images = []
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
    else:
        form = ImageForm()

    try:
        images = Image.objects.all()
    except Image.DoesNotExist:
        images = None
    return render(request , 'profile.html' , { 'images': images, 'form': form })

def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new_bio = form.cleaned_data["bio"]
            new_pic = form.cleaned_data["pic"]
            profile = Profile.objects.get(user = request.user)
            profile.bio = new_bio
            profile.pic = new_pic
            profile.save()
            final_url = "/profile/" + str(request.user.id) + "/"
            return redirect(final_url)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form":form}) 