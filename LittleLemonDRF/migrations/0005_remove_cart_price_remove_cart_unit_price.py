# Generated by Django 4.1.5 on 2023-01-04 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0004_alter_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='unit_price',
        ),
    ]
