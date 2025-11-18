from django.db import models

class BrandCar(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Название Бренда'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бранд'
        verbose_name_plural = 'Бранды'

