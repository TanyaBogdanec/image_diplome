# Generated by Django 5.0 on 2023-12-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_and_image', '0004_alter_image_file_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_img',
            field=models.ImageField(upload_to='images/', verbose_name='File image'),
        ),
    ]
