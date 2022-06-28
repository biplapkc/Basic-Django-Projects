from django import forms
class usersForm(forms.Forms):
    num1=forms.CharField(label="Fisrt Number", max_length=20, required=True)
    num2=forms.forms.CharField(label="Second Number", max_length=20, required=True)
