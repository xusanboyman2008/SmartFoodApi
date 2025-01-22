from rest_framework import viewsets

from api.Serializer import ProductSerializer, CategorySerializer, CheckoutSerializer, ProductQuantitySerializer, \
    SpacialOfferSerializer
from products.models import Product, Category, Checkout, ProductQuantity, SpacialOffer


class SpacialOfferViewSet(viewsets.ModelViewSet):
    queryset = SpacialOffer.objects.all()
    serializer_class = SpacialOfferSerializer


class ProductQuantityViewSet(viewsets.ModelViewSet):
    queryset = ProductQuantity.objects.all()
    serializer_class = ProductQuantitySerializer


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

