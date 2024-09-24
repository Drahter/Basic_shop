from django.contrib import admin

from blog.models import BlogArticle


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'views_counter',)
    search_fields = ('title', 'content',)
