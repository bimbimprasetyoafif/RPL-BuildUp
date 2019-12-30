from rest_framework import serializers
from .models import Design, RAB, DesignImages, MaterialAtap, MaterialDinding, MaterialLantai, MaterialPlafon, MaterialCatLuar, MaterialCatDalam
from rest_framework.fields import empty


class DesignImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DesignImages
        fields = "__all__"

class DesignRABSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RAB
        fields = "__all__"

class DesignSerializer(serializers.ModelSerializer):
    allImagesDesign= DesignImagesSerializer(many=True, read_only=True)
    allRAB= DesignRABSerializer(many=True, read_only=True)

    class Meta:
        model = Design
        fields = "__all__"

# adaddadadadad

class MaterialAtapSerializer(serializers.ModelSerializer):
    CustomAtap= DesignSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialAtap
        fields = "__all__"

class MaterialPlafonSerializer(serializers.ModelSerializer):
    CustomPlafon= DesignSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialPlafon
        fields = "__all__"

class MaterialLantaiSerializer(serializers.ModelSerializer):
    CustomLantai= DesignSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialLantai
        fields = "__all__"

class MaterialDindingSerializer(serializers.ModelSerializer):
    CustomDinding= DesignSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialDinding
        fields = "__all__"

class MaterialCatInteriorSerializer(serializers.ModelSerializer):
    CustomCatDalam= DesignSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialCatDalam
        fields = "__all__"

class MaterialCatExteriorSerializer(serializers.ModelSerializer):
    CustomCatLuar= DesignSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialCatLuar
        fields = "__all__"