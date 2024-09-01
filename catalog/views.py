from django.shortcuts import render
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def new_product(request):
    return render(request, 'new_product.html')
