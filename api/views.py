from flask import redirect
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.Serializer import ProductSerializer, CategorySerializer, CheckoutSerializer, ProductQuantitySerializer
from products.models import Product, Category, Checkout, ProductQuantity



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
    filter_backends = [SearchFilter]
    search_fields = ['category__name']

    def get_queryset(self):
        """
        Optionally restrict the returned products to a specific category
        by filtering against the `category_name` query parameter in the URL.
        """
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category_nam e', None)
        if category_name:
            queryset = queryset.filter(category__name__icontains=category_name)
        return queryset


def res(request):
    return redirect('api')