# Generated by Django 5.1 on 2024-09-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_merge_20240910_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogarticle',
            options={'verbose_name': 'статья блога', 'verbose_name_plural': 'статьи блога'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='цена'),
        ),
    ]
