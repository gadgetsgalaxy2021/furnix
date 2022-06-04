from django.contrib import admin

# Register your models here.

from .models import Category, Contact_Us, Order, Sub_Category, Product

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact_Us)
admin.site.register(Order)