# Generated by Django 5.1 on 2024-08-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_category_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_created=True, null=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата изменения'),
        ),
    ]
