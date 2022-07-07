from django.contrib import admin
from news.models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=('News_Title','News_Description')

admin.site.register(News,NewsAdmin)

