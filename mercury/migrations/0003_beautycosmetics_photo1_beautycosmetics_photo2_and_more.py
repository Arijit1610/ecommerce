# Generated by Django 5.0.2 on 2024-03-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercury', '0002_beautycosmetics_booksandstationery_eletronices_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautycosmetics',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='beautycosmetics',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='beautycosmetics',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='beautycosmetics',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='booksandstationery',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='booksandstationery',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='booksandstationery',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='booksandstationery',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='eletronices',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='eletronices',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='eletronices',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='eletronices',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='fashion',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='fashion',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='fashion',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='fashion',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='homeandkitchen',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='homeandkitchen',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='homeandkitchen',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='homeandkitchen',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='sportsooutdoor',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='sportsooutdoor',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='sportsooutdoor',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='sportsooutdoor',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
    ]
