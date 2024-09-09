from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='prod_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='new_product'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
