from django.urls import path
from app.product.views import BrandCarAPIView, BrandCarCreateAPIView

urlpatterns = [
    path("list-brand/", BrandCarAPIView.as_view(), name='list-brand'),
    path("create-brand/", BrandCarCreateAPIView.as_view(), name='create-brand'),
]
