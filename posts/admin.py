from django.contrib import admin
from posts.models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display=('Title','Description')

admin.site.register(News,NewsAdmin)