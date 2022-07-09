import imp
from pyexpat import model
from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=50)
    Description=HTMLField()
