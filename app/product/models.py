from django.db import models
from app.product.contants import TYPE_CAR

class BrandCar(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Название Бренда'
    )
    type_car = models.CharField(
        max_length=15,
        verbose_name='Тип машины', 
        choices=TYPE_CAR,
        default=None
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бранд'
        verbose_name_plural = 'Бранды'

class ModelCar(models.Model):
    brand = models.ForeignKey(
        BrandCar,
        on_delete=models.SET_NULL,
        related_name='brand',
        verbose_name='Бранл',
        blank=True, null=True
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Модель'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'