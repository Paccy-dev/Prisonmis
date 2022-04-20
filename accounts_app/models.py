from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        return self.firstname + ' ' + self.lastname


class User(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


@receiver(post_save, sender=Employee)
def create_product(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(username=instance.firstname, password='user1234', employee=instance)
