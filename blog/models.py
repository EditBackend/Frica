from django.db import models

# Create your models here.

#  👉-------------------------------------------dinamik modellar uchun --------------------------------------------👈

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salePrice = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    img1 = models.ImageField(upload_to='category/')
    img2 = models.ImageField(upload_to='category/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# 👉-------------------------------------------dinamik modellar uchun  end--------------------------------------------👈



