# Generated by Django 4.0.2 on 2022-05-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnix', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
