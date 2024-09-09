from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product

    # app_name/<model_name>_<action>


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("category:prod_list")


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("category:prod_list")