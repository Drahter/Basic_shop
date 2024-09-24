from django.urls import path
from blog.apps import BlogConfig

from blog.views import BlogArticleListView, BlogArticleDetailView, BlogArticleUpdateView, BlogArticleDeleteView, \
    BlogArticleCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogArticleListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogArticleDetailView.as_view(), name='article_detail'),
    path('blog/create/', BlogArticleCreateView.as_view(), name='article_create'),
    path('blog/<int:pk>/update/', BlogArticleUpdateView.as_view(), name='article_update'),
    path('blog/<int:pk>/delete/', BlogArticleDeleteView.as_view(), name='article_delete'),
]