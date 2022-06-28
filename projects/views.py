
from django.http import HttpResponse
from django.shortcuts import render
from .forms import usersForm

def home(request):
    return render(request,"index.html")

def calculator(request):
    full=""
    data={}
    try:
        if request.method=="POST":
            f=request.POST.get('fname')
            l=request.POST.get('lname')
            full=f+l
            print(full)
            data={
                "firstName":f,
                "lastName":l,
                "fullName":full
            }
    except:
        pass

    return render(request,"index.html",data)