from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='категория', max_length=50, unique=True)

class Product(models.Model):
    title = models.CharField(verbose_name='продукт', max_length=50, unique=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
