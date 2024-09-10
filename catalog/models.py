from django.db import models


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

    def __str__(self):
        return f'{self.name}, категория {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class BlogArticle(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='слаг')
    content = models.TextField(verbose_name='содержание')
    preview_image = models.ImageField(verbose_name='изображение')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)
    views_counter = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'статья блога'
        verbose_name_plural = 'статьи блога'
