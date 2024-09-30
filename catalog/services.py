from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "categories_list"
    categories = cache.get(key)
    if categories is not None:
        return categories

    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
