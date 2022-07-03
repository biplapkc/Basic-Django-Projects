from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_name','service_des')

admin.site.register(Service,ServiceAdmin)

# Register your models here.
