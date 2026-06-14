from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение"
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Категория"
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
