from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование', null=True)
    description = models.TextField(max_length=500, verbose_name='описание', null=True)
    image = models.ImageField(verbose_name='изображение', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.IntegerField(verbose_name='цена', null=True)
    created_at = models.DateTimeField(verbose_name='дата создания', null=True, auto_created=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', null=True, auto_now_add=True)
    views_counter = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)
    is_active = models.BooleanField(verbose_name='опубликован', default=False)

    creator = models.ForeignKey(User, verbose_name='Автор', help_text='Укажите автора товара', null=True, blank=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}, категория {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('can_edit_description', 'Can edit description'),
            ('can_edit_is_active', 'Can hide products'),
            ('can_edit_category', 'Can change category'),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='текущая версия', default=False)

    def __str__(self):
        return f'Версия {self.version_number} продукта {self.product.name}'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продуктов'
