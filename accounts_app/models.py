from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50, default='Not_provided')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, default='Not_provided')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstname = models.CharField(max_length=30, default='Not_provided')
    lastname = models.CharField(max_length=30, default='Not_provided')
    email = models.EmailField()
    Identification = models.IntegerField()
    phone = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='photos/', default='avatar.png')

    def __str__(self):
        return self.firstname


class User(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
