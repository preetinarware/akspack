import imp
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(contact_msg)

class contact_msg(admin.ModelAdmin):
    list_display=['name','subject']