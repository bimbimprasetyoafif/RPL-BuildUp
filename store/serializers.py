from rest_framework import serializers
from .models import Stores
from products.serializers import ProductSerializer

class StoresSerializer(serializers.ModelSerializer):
    ProductItems = ProductSerializer(many=True)
    class Meta:
        model = Stores
        # fields = ['StoreId', 'StoreName', 'StoreAddress', 'StoreImage', 'ProductItems']
        fields = "__all__"



