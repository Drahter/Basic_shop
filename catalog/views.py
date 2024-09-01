from django.shortcuts import render
from catalog.models import Product, Category


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def new_product(request):
    categories = Category.objects.all()
    context = {"products": categories}
    return render(request, 'new_product.html', context)
