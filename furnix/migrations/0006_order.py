# Generated by Django 4.0.2 on 2022-05-20 07:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('furnix', '0005_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='esite/order/image')),
                ('quantity', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furnix.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
