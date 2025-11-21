from django.shortcuts import render
from rest_framework import generics

from app.product.models import BrandCar, ModelCar
from app.product.serializers import BrandCarSerializers, ModelCarSerilaizer

class BrandCarAPIView(generics.ListAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers

class BrandCarCreateAPIView(generics.CreateAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers

class BrandCarReadAPIView(generics.RetrieveAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers

class BrandCarUpdateAPIView(generics.UpdateAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers

class BrandCarDeleteAPIView(generics.DestroyAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializers


############333#######
class ModelCarAPIView(generics.ListAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerilaizer

class ModelCarCreateAPIView(generics.CreateAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerilaizer

class ModelCarReadAPIView(generics.RetrieveAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerilaizer

class ModelCarUpdateAPIView(generics.UpdateAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerilaizer

class ModelCarDeleteAPIView(generics.DestroyAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerilaizer