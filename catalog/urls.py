from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, BlogArticleListView, BlogArticleDetailView, BlogArticleUpdateView, BlogArticleDeleteView, \
    BlogArticleCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='new_product'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('blog/', BlogArticleListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogArticleDetailView.as_view(), name='article_detail'),
    path('blog/create/', BlogArticleCreateView.as_view(), name='article_create'),
    path('blog/<int:pk>/update/', BlogArticleUpdateView.as_view(), name='article_update'),
    path('blog/<int:pk>/delete/', BlogArticleDeleteView.as_view(), name='article_delete')
]
