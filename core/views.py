from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import user_logged_in,get_user



def index(request):
    return render(request,'index.html')
