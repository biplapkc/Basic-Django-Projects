from django import forms

class users(forms.Form):
    fname=forms.CharField(label="First Name")
    lname=forms.CharField(label="Last Name")

    
    email=forms.EmailField(label="E-mail")
