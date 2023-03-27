from django.contrib import admin
from product.models import Product
# from .models import Image

# Register your models here.
# @admin .register(Image)
# class Imageadmin(admin.modeks.ModelAdmin):
#     list_display=['name','price','image','quality'] 
admin.site.register(Product)
