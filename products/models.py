from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Category(models.Model):
    """Model representing a product category"""
    name = models.CharField(max_length=35, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()   # Normalize the name to lowercase before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    """
    This constraint prevents the database from accepting duplicates 
    based on case-insensitive comparisons.
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"], name="unique_category_name", condition=models.Q(name__iexact=models.F("name"))
            )
        ]


class Product(models.Model):
    """Model representing a product in the store"""
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, related_name="products")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name="product_created")
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name