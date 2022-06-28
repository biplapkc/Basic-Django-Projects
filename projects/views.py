import imp
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .forms import usersForm

def home(request):
    return render(request,"index.html")

def users(request):
    fn=usersForm()
    data={}
    try:
        if request.method=="POST":
            f=request.POST.get('fname')
            l=request.POST.get('lname')
            fullName=f+l
            data={
                "firstName":f,
                "lastName":l,
                "fullName":full
            }
    except:
        pass



