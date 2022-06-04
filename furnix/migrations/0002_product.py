# Generated by Django 4.0.2 on 2022-03-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ESITE/img')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
