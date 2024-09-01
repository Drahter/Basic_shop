from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, new_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='prod_list'),
    path('contacts/', contacts, name='contacts'),
    path('new_product/', new_product, name='new_product')

]
