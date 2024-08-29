from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование', null=True)
    description = models.TextField(max_length=500, verbose_name='описание', null=True)

    def __str__(self):
        pass

    class Meta:
        pass


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование', null=True)
    description = models.TextField(max_length=500, verbose_name='описание', null=True)
    image = models.ImageField(verbose_name='изображение', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name='цена', null=True)
    created_at = models.DateTimeField(verbose_name='дата создания', null=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', null=True)

    def __str__(self):
        pass

    class Meta:
        pass
