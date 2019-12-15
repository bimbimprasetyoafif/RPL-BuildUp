from rest_framework import serializers
from .models import Vendors
# from products.serializers import ProductSerializer

class VendorsSerializer(serializers.ModelSerializer):
    # ProductItems = ProductSerializer(many=True)
    class Meta:
        model = Vendors
        fields = "__all__"



