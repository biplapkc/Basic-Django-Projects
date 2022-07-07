from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class News(models.Model):
    News_Title=models.CharField(),
    News_Description=HTMLField()
