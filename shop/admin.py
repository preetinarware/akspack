from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(productDetail)

admin.site.register(productThickness)

admin.site.register(productStyle)

admin.site.register(productSize)

admin.site.register(productMaterial)

admin.site.register(productCategory)


admin.site.register(productUses)

admin.site.register(coupons)

admin.site.register(prices)
