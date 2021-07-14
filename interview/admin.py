from django.contrib import admin
from .models import *

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user','question_text', 'timer',]
    list_filter =  ['user','question_text', 'timer',]
    list_display_links =  ['user','question_text', 'timer']


admin.site.register(Question,QuestionAdmin)
admin.site.register(Interview)