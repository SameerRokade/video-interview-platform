from django.contrib import admin
from .models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','full_name', 'email','account_type']
    list_filter =  ['user','full_name', 'email','account_type']
    list_display_links =  ['user','full_name', 'email','account_type']





admin.site.register(Profile,ProfileAdmin)


