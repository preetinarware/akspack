from distutils.command.upload import upload
from operator import mod
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from shop.models import slug_generator
from ckeditor.fields import RichTextField

class blog_detail(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posted_by')
    slug=models.SlugField(unique=True,max_length=1000)
    blog_img=models.ImageField(upload_to='blog')
    blog_name=models.CharField(max_length=150)
    blog_category=models.CharField(max_length=100)
    blog_description=RichTextField(validators=[MinLengthValidator(200)])
    created_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.slug == '' or len(self.slug)==0:
            self.slug = slug_generator(blog_detail,self.blog_name)
        super(blog_detail, self).save(*args, **kwargs)
  
    def __str__(self):
        return self.slug
        # validators=[MaxLengthValidator(200)]