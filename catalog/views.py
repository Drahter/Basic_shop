from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product

    # app_name/<model_name>_<action>


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    return render(request, 'contacts.html')


def new_product(request):
    categories = Category.objects.all()
    context = {"catalog": categories}
    return render(request, 'new_product.html', context)

# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)
