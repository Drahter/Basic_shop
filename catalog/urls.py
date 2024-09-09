from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, new_product, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='prod_list'),
    path('contacts/', contacts, name='contacts'),
    path('new_product/', new_product, name='new_product'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail')

]
