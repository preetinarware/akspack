from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class frgt_pwd(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='pwd')
    frg_token=models.CharField(max_length=1000)
    def __str__(self):
        return self.user.username