from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created_at')

    def __str__(self):
        return self.name_category


class Image(models.Model):
    file_img = models.ImageField(upload_to='images/', verbose_name='File image')
    description = models.TextField(max_length=2500, verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    delete = models.BooleanField()
    uploaded_at = models.DateTimeField(default=timezone.now, verbose_name='Uploaded at')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Updated at')
    deleted_at = models.DateTimeField(default=timezone.now, verbose_name='Deleted at')

    def __str__(self):
        return self.user.username

