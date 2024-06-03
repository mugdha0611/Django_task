from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('electronics', 'Electronics'),
        ('home_kitchen', 'Home & Kitchen'),
    ]

    name = models.CharField(max_length=200)
    shape = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name