
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import users
from service.models import Service
from posts.models import News

def home(request):
    form=users()
    data={}
    if request.method=="POST":
        form=users(request.POST)

        if form.is_valid():
            fname=form.cleaned_data('fname')
            lname=form.cleaned_data('lname')
            email=form.cleaned_data('email')
            data={
                'fname':fname,
                'lname':lname,
                'email':email,
                'form':form
            }

            return HttpResponseRedirect('/calc')

        else:
            form=users()

            

    return render(request,'index.html',{'form':form})


def calculator(request):
    ans=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('operators')
    
            if opr=="+":
                ans=n1+n2

            elif opr=="-":
                ans=n1-n2

            elif opr=="*":
                ans=n1*n2

            elif opr=="/":
                ans=n1/n2
            

    except:
        c="Invalid operator or input"

        

    return render(request,'calculator.html',{'ans':ans})


def ourservices(request):
    #servicesData=Service.objects.all().order_by('service_name')[:2] // it gets 2 data from admin
    #servicesData=Service.objects.all() // it gets all the data from admin 

    #To filter from search 
    servicesData=Service.objects.all()
    if request.method=="GET":
        st=request.GET.get('inputService')
        if st!=None:
            #servicesData=Service.objects.filter(service_name=st) // searches if matches the whole word

            #to search with a single letter if matches
            servicesData=Service.objects.filter(service_name__icontains=st)

    data={
        'servicesData':servicesData
    }

    return render(request,"ourservices.html",data)


def allNews(request):
    newsData=News.objects.all()
    data={
        'newsData':newsData
    }

    return render(request,'news.html',data)