from django.contrib import admin
from catalog.models import Category, Product, BlogArticle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category', )
    search_fields = ('name', 'description',)


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'views_counter',)
    search_fields = ('title', 'content',)
