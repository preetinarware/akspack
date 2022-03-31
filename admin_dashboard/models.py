from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class setting(models.Model):
    logo = models.ImageField(upload_to="logo")
    title = models.CharField(max_length=30)
    favicon  = models.ImageField(upload_to='logo')
    def __str__(self) -> str:
        return self.title
    
class admin_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='admin_record')
    name=models.CharField(max_length=30)
    email = models.EmailField()
    img=models.ImageField(upload_to='img/',null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    address=models.TextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.name