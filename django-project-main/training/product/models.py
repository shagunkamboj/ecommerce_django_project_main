from django.db import models
from django.contrib.auth.models import User
#from product.models import ProductVariation
# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.tag_name
class Product(models.Model):
    name =models.CharField(max_length=50)
    price=models.IntegerField(null= True)
    quantity = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',null = True)
    category = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag,null = True)
    def __str__(self):
        return self.name
class Cart(models.Model):
  product1 = models.ForeignKey(Product, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity = models.CharField(max_length=30)

class AddressModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=1024)
    address = models.CharField( max_length=1024)
    city = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=14)

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    total_cost = models.FloatField(default=1)
    date = models.DateTimeField(auto_now=True)
    
    mobile_no = models.CharField(max_length = 12)
    product = models.ForeignKey(Product,  related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
  
class Wishlist(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

class Order_item(models.Model):
    price_item = models.CharField(max_length=200)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
