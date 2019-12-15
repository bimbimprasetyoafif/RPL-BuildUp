from rest_framework import serializers
from .models import Categorys
from products.serializers import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    ProductInCategory = ProductSerializer(many=True)
    class Meta:
        model = Categorys
        fields = "__all__"



