from django.db import models

from User.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class SpacialOffer(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    expiration_date = models.DateField(null=False)

    class Meta:
        ordering = ['-expiration_date', 'discount']

    def __str__(self):
        return f"{self.discount}% until {self.expiration_date}"


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)
    description = models.TextField(null=False)
    image = models.ImageField(null=False,upload_to='media')
    animation = models.ImageField(default='no', blank=True,upload_to='media')
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    # special_offer = models.ForeignKey(SpacialOffer, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


    class Meta:
        ordering = ['category']


class ProductQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return f"ProductQuantity ID: {self.id}"



class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductQuantity, related_name="checkouts")
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    total_price = models.FloatField(default=0, blank=True)
    delivery_cost = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    checkouts = models.ManyToManyField(Checkout, related_name="basket_id")
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id']
