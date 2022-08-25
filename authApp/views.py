import imp
from multiprocessing import context
import re
from tkinter.messagebox import RETRY
from django.shortcuts import render , redirect
from django.http import HttpResponse
from . forms import CreateUser
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUser()

        if request.method == "POST":
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request , "Your account has been created !")
                return redirect("login")

        context = {"form": form}
        return render(request , 'authApp/register.html' , context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username , password = password)
            
            if user is not None:
                login(request , user)
                return redirect('home')
            else:
                messages.info(request , 'Username OR password is incorrect!')

        context = {}
        return render(request , 'authApp/login.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def HomePage(request):
    return render(request , 'authApp/home.html')
