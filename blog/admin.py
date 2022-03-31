from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(blog_detail)
class blog(admin.ModelAdmin):
    exclude = ('slug',)
    list_display=['blog_name'[:30],'posted_by']

    