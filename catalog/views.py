from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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



def contacts(request):
    return render(request, 'contacts.html')


