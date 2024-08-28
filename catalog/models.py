from django.db import models


class Product(models.Model):
    pass

    def __str__(self):
        name = models.CharField(max_length=50, verbose_name='наименование')
        description = models.TextField(max_length=500, verbose_name='описание')
        image = models.ImageField(verbose_name='изображение')
        category = models.ForeignKey(Category, on_delete=models.SET_NULL)
        price = models.IntegerField(max_length=10, verbose_name='цена')
        created_at = models.DateTimeField(verbose_name='дата создания')
        updated_at = models.DateTimeField(verbose_name='дата изменения')

    class Meta:
        pass


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    def __str__(self):
        pass

    class Meta:
        pass
