# Generated by Django 4.0.5 on 2022-11-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_products_color_variant_products_size_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='color_variant',
            field=models.ManyToManyField(blank=True, to='product.colorvariant'),
        ),
        migrations.AlterField(
            model_name='products',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='product.sizevariant'),
        ),
    ]
