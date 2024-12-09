from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

STATUS_PENDING = "PENDING"
STATUS_IN_TRANSIT = "IN_TRANSIT"
STATUS_DELIVERED = "DELIVERED"

ORDER_STATUS = [
    (STATUS_PENDING, "Pending"),
    (STATUS_IN_TRANSIT, "In Transit"),
    (STATUS_DELIVERED, "Delivered"),
]


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="orders")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="orders")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default=STATUS_PENDING)

    def __str__(self):
        return f"Order No.{self.id} -> {self.status}"