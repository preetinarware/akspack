# from asyncio import transports
# from distutils.command.upload import upload
# from operator import mod
# from random import choice
# from turtle import color
# from unicodedata import category
from django.db import models

from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.text import slugify

import random ,string
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))
def slug_generator(instance, new_slug=None):
    slug=slugify(new_slug)[:50]
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = slugify(str(slug)[:46]+get_random_string(4))
        return slug_generator(instance, new_slug=new_slug)
    return slug


choice_size_type = (
        ('cm', 'cm'),
        ('MM', 'MM'),
        ('Inch', 'Inch'),)  

class productSize(models.Model):
    size_id=models.CharField(max_length=100,blank=True)
    meassuement=models.CharField(max_length=10,choices=choice_size_type, verbose_name = 'size')
    min=models.IntegerField()
    max=models.IntegerField()
    lenght=models.IntegerField()
    width=models.IntegerField()
    height=models.IntegerField()
    #    self.meassuement
    def save(self, *args, **kwargs):
        if self.id:
            self.size_id = "size"+str(self.id)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.meassuement


class productThickness(models.Model):
    # thick_id=models.CharField(max_length=100,blank=True)
    thickness=models.IntegerField()
    # def save(self, *args, **kwargs):
    #     if self.id:
    #         self.cat_id = "thick"+str(self.id)
    #     super().save(*args, **kwargs)
    
    
class productMaterial(models.Model):
    
    # mate_id=models.CharField(max_length=100,blank=True)
    material=models.CharField(max_length=200)
    # def save(self, *args, **kwargs):
    #     if self.id:
    #         self.mate_id = self.material[:15]+str(self.id)
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.material


class productStyle(models.Model):
    
    # col_id=models.CharField(max_length=100,blank=True)
    color=models.CharField(max_length=200)
    # def save(self, *args, **kwargs):
    #     if self.id:
    #         self.col_id = self.color[:15]+str(self.id)
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.color


class productCategory(models.Model):
    
    # cat_id=models.CharField(max_length=100,blank=True)
    category=models.CharField(max_length=200)
    # def save(self, *args, **kwargs):
        # if self.id:
        #     self.cat_id = self.category[:15]+str(self.id)
        # super().save(*args, **kwargs)
    def __str__(self):
            return self.category

class productUses(models.Model):
    
    # use_id=models.CharField(max_length=100,blank=True)
    slug=models.SlugField(unique=True,max_length=1000)
    uses=models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        if self.slug == '' or len(self.slug)==0:
            self.slug = slug_generator(productUses,self.uses)
        super().save(*args, **kwargs)
        # if self.id:
        #     self.use_id = self.uses[:15]+str(self.id)
        # super().save(*args, **kwargs)
    def __str__(self):
        return self.uses


class coupons(models.Model):
    coupan_code=models.IntegerField(default=0)
    Coupon_id = models.CharField(max_length=50,blank=True)
    coupan_name = models.CharField(max_length=50)
    Coupon_expire_date = models.DateField()
    quantity = models.IntegerField(default=100)
    used = models.IntegerField(default=0)
    remaining = models.IntegerField(default=0)
    Coupon_created = models.DateField(auto_now=True) 
    message = models.CharField(max_length=100,help_text="User will see this messge when he/she apply the coupen",default='Applied')
    discount = models.CharField(help_text="You Can Ammount or Percent of Ammount Eg: 100 or 10%",max_length=10)
    minimum_order_value = models.FloatField()
    def __str__(self):
        return F"{self.coupan_name} - ( {self.Coupon_id} )"
    def save(self, *args, **kwargs):
    
        self.remaining = self.quantity - self.used
        super().save(*args, **kwargs)
        if len(self.Coupon_id)<1:
            self.Coupon_id = self.coupan_name+str(self.id)
        super().save(*args, **kwargs)
    # def clean(self):
    #     discount = self.discount.replace('%','')
    #     try:
    #         discount = float(discount)
    #     except:
    #         raise ValidationError(
    #             {'discount': "Please add a valid discount"})
    #     if '%' in self.discount:
    #         if not (discount <=100):
    #             raise ValidationError(
    #             {'discount': "discount should be under 100%"})



class productDetail(models.Model):
    product_id=models.CharField(max_length=50,blank=True)
    slug=models.SlugField(unique=True,max_length=1000)
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='product')
    # price=models.IntegerField()
    # discount=models.IntegerField(default=0)
    # pricebase=models.IntegerField()
    # transports=models.IntegerField()
    # gst=models.IntegerField()
    min_pack_ordr=models.IntegerField(default=0)
    
    material=models.ManyToManyField(productMaterial)
    uses=models.ManyToManyField(productUses)


    # thickness=models.ManyToManyField(productThickness)
    # material=models.ManyToManyField(productMaterial)
    # color=models.ManyToManyField(productStyle)
    # category=models.ForeignKey(productCategory,on_delete=models.CASCADE)
    # uses=models.ManyToManyField(productUses)
    # size=models.ManyToManyField(productSize)
    
    quntity=models.IntegerField()
    about=models.TextField()
    long_description=models.TextField()
    def save(self, *args, **kwargs):
        if self.slug == '' or len(self.slug)==0:
            self.slug = slug_generator(productDetail,self.name)
        super(productDetail, self).save(*args, **kwargs)
        if self.product_id == '' or len(self.product_id)==0:
            self.product_id = self.name+str(self.id)
        super().save(*args, **kwargs)
    # def clean(self):
    #     discount = self.discount.replace('%','')
    #     try:
    #         discount = float(discount)
    #     except:
    #         raise ValidationError(
    #             {'discount': "Please add a valid discount"})
    #     if '%' in self.discount:
    #         if not (discount <=100):
    #             raise ValidationError(
    #             {'discount': "discount should be under 100%"})

    def __str__(self):
        return self.product_id


class prices(models.Model):
    product=models.OneToOneField(productDetail,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    price_base=models.IntegerField()
    transports=models.IntegerField(default=0)
    gst=models.IntegerField(default=0)

    thickness=models.ManyToManyField(productThickness)
    color=models.ManyToManyField(productStyle)
    category=models.ForeignKey(productCategory,on_delete=models.CASCADE)
    size=models.ManyToManyField(productSize)
    def save(self, *args, **kwargs):
        if self.price == '' or self.price==0 or self.price:
            # dis=
            self.price = int(self.price_base)+int(self.gst)+int(self.transports)
            if self.discount!=0:
                self.price = int(self.price)-(int(self.price_base)*(int(self.discount)/100))
            
        super().save(*args, **kwargs)
        
   