from distutils.command.upload import upload
from email.mime import image
from itertools import product
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Product(models.Model):
    Availability = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
    image = models.ImageField(upload_to = 'ecomers/img')
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    details = models.TextField(default='')
    Availability = models.CharField(choices=Availability,null=True,max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact_Us(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

class Order(models.Model):
    image = models.ImageField(upload_to='esite/order/image')
    product = models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    total = models.CharField(max_length=1000, default='')
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.product