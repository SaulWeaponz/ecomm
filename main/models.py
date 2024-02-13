from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserProfile(AbstractBaseUser):
    user_id = models.CharField(primary_key=True, unique=True, max_length=15)
    phone_number = models.CharField(max_length=10)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "email"]


class Brand(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=100, null=True, blank=True)


class Cart(models.Model):
    pass
