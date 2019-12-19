from rest_framework import serializers
from .models import Products, ProductImages
from rest_framework.fields import empty


class ProductImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImages
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    ImagesProduct = ProductImagesSerializer(many=True)

    class Meta:
        model = Products
        fields = "__all__"

    def create(self, validated_data):
        tracks_data = validated_data.pop('ImagesProduct')
        produk = Products.objects.create(**validated_data)
        for track_data in tracks_data:
            Products.objects.create(produk=produk, **track_data)
        return produk



