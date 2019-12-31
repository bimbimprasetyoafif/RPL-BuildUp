from rest_framework import serializers
from .models import Categorys,CategorysHome
from products.serializers import ProductSerializer
from design.serializers import DesignSerializer

class CategorySerializer(serializers.ModelSerializer):
    productInCategory = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Categorys
        fields = "__all__"

class CategoryHomeSerializer(serializers.ModelSerializer):
    designInCategory = DesignSerializer(many=True)
    class Meta:
        model = CategorysHome
        fields = "__all__"

