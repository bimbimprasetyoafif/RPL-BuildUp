from rest_framework import serializers
from .models import ProductOwner, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProdcutOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOwner
        fields = "__all__"

