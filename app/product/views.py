from django.shortcuts import render
from rest_framework import generics

from app.product.models import BrandCar
from app.product.serializers import BrandCarSerializers

class BrandCarAPIView(generics.ListAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers

class BrandCarCreateAPIView(generics.CreateAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers