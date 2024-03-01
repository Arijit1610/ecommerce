# Generated by Django 5.0.2 on 2024-02-29 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('cloth_name', models.CharField(max_length=100)),
                ('cloth_type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('qty', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('discount', models.IntegerField()),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercury.product')),
            ],
        ),
    ]
