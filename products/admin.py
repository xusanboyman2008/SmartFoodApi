from django.contrib import admin
from django.contrib.admin import site

from products.models import Product, Category, Checkout, ProductQuantity

# Register your models here.
site.register(Product)
site.register(Category)
site.register(Checkout)
site.register(ProductQuantity)
