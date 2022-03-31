from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.


admin.site.register(frgt_pwd)
# class pwd(admin.ModelAdmin):

#     list_display=['user']
