from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer =models.BooleanField(default=False)
    is_seller =models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='Customer')
    name =models.CharField(max_length=20)
    email =models.EmailField()
    phone_number =models.CharField(max_length=10)

class Seller(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='Seller')
    name =models.CharField(max_length=20)
    email =models.EmailField()
    phone_number =models.CharField(max_length=10)

class Blog(models.Model):
    Customer_name =models.ForeignKey('Customer',on_delete=models.CASCADE)
    title =models.CharField(max_length=30)
    content =models.TextField()
    author_name =models.CharField(max_length=30)
    date =models.DateField()
    document = models.FileField(upload_to='documents/')