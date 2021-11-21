from django.db import models


class Product(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass