from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=50, default='Not_provided')
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='photos/', default='avatar.png')

