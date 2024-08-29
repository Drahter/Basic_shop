from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('category', )
    search_fields = ('name', 'description',)
