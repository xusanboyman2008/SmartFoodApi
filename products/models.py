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


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)
    description = models.TextField(null=False)
    image = models.ImageField(null=True, upload_to='media',blank=True)
    animation = models.ImageField(default='no', blank=True, upload_to='media', null=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    # special_offer = models.ForeignKey(SpacialOffer, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ['category']


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    expired_at = models.DateTimeField()


class ProductQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return f"ProductQuantity ID: {self.id}"


class Location_User(models.Model):
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.TextField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class State_For_State(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField(null=False)


class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductQuantity, related_name="checkouts")
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    total_price = models.FloatField(default=0, blank=True)
    address = models.TextField(null=False)
    delivery_cost = models.FloatField(default=0, null=True, blank=True)
    delivery_option = models.TextField(null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)
    status = models.CharField(max_length=100, default='Tastiqlamoqda')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
