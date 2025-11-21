from django.urls import path
from app.product.views import (
    BrandCarAPIView, BrandCarCreateAPIView, BrandCarReadAPIView,
    BrandCarUpdateAPIView, BrandCarDeleteAPIView,

    ModelCarAPIView, ModelCarCreateAPIView, ModelCarReadAPIView,
    ModelCarUpdateAPIView, ModelCarDeleteAPIView
)

urlpatterns = [
    path("list-brand/", BrandCarAPIView.as_view(), name='list-brand'),
    path("create-brand/", BrandCarCreateAPIView.as_view(), name='create-brand'),
    path("brands/<int:pk>/", BrandCarReadAPIView.as_view(), name='read-brand'),
    path("brands/<int:pk>/update", BrandCarUpdateAPIView.as_view(), name='update-brand'),
    path("brands/<int:pk>/delete", BrandCarDeleteAPIView.as_view(), name='delete-brand'),

    path("list-Model/", ModelCarAPIView.as_view(), name='list-Model'),
    path("create-Model/", ModelCarCreateAPIView.as_view(), name='create-Model'),
    path("Models/<int:pk>/", ModelCarReadAPIView.as_view(), name='read-Model'),
    path("Models/<int:pk>/update", ModelCarUpdateAPIView.as_view(), name='update-Model'),
    path("Models/<int:pk>/delete", ModelCarDeleteAPIView.as_view(), name='delete-Model'),
]
