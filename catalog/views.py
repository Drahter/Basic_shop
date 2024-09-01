from django.shortcuts import render
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'home.html', context)


def contacts(request):
    return render(request, 'contacts.html')
