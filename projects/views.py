import re
from django.shortcuts import render
from .forms import NameForm

def home(request):
    return render(request,'index.html')

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