from rest_framework import serializers
from app.product.models import BrandCar

class BrandCarSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandCar
        fields = ['id', 'title']