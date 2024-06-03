from django.db import models
from products.models import Product
from accounts.models import UserProfile

class Recommendation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} recommended for {self.user.user.username}"