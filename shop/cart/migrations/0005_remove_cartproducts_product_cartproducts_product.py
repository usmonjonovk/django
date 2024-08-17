# Generated by Django 5.0.2 on 2024-08-16 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_cartproducts_product_cartproducts_product'),
        ('main', '0002_product_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproducts',
            name='product',
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
            preserve_default=False,
        ),
    ]
