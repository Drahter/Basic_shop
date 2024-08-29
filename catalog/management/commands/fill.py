from django.core.management import BaseCommand
import json

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        categories = []
        with open('catalog/fixtures/catalog_data.json', 'r',
                  encoding='utf8') as file:
            data = json.load(file)
            for each in data:
                if each['model'] == 'catalog.category':
                    categories.append(each)

        return categories

    @staticmethod
    def json_read_products():
        products = []
        with open('catalog/fixtures/catalog_data.json', 'r',
                  encoding='utf8') as file:
            data = json.load(file)
            for each in data:
                if each['model'] == 'catalog.product':
                    products.append(each)

        return products

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'], name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']
                        )
            )

        Product.objects.bulk_create(product_for_create)
