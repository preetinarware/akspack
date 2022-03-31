from django.db import models
from django.contrib.auth.models import *
# Create your models here.

class contact_msg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=500)
    Msg=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name