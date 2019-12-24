from rest_framework import serializers
from .models import Products, ProductImages
from rest_framework.fields import empty


class ProductImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImages
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    allImagesProduct = ProductImagesSerializer(many=True, read_only=True)
    # creator = serializers.IntegerField(read_only=)
    # creator = serializers.ReadOnlyField(read_only=True)
    # creator = serializers.PrimaryKeyRelatedField(required=False, queryset=Products.objects.all())
    # creator = serializers.ReadOnlyField(required=False)

    class Meta:
        model = Products
        fields = "__all__"

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('ImagesProduct')
    #     produk = Products.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Products.objects.create(produk=produk, **track_data)
    #     return produk



