# Generated by Django 4.0.2 on 2022-05-21 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnix', '0011_remove_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(default=''),
        ),
    ]