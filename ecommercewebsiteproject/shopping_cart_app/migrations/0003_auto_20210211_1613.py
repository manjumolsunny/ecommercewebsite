# Generated by Django 3.1.5 on 2021-02-11 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart_app', '0002_product_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('desc',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
