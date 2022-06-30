from django import forms
from django.shortcuts import render

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
