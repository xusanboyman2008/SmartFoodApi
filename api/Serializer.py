from rest_framework import serializers

from products.models import Product, Checkout, ProductQuantity, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(source='category', read_only=True)  # Read-only detailed category
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                  write_only=True)  # Write-only for category

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'description', 'price', 'status',
            'image', 'animation', 'categories', 'created_at', 'updated_at'
        ]


class ProductQuantitySerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only=True, source='product')  # Read-only field for product details

    class Meta:
        model = ProductQuantity
        fields = ['id', 'product_id', 'quantity', 'product']


class CheckoutSerializer(serializers.ModelSerializer):
    product_details = ProductQuantitySerializer(source='products', many=True, read_only=True)
    products = serializers.PrimaryKeyRelatedField(queryset=ProductQuantity.objects.all(), many=True, write_only=True)

    class Meta:
        model = Checkout
        fields = [
            'id', 'user', 'products', 'product_details', 'latitude',
            'longitude', 'created_at', 'delivery_cost', 'total_price'
        ]
