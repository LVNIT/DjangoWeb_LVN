from django.db import models
from django.conf import settings

from store.models import Shoe


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail')
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name='shoe_detail')

    price = models.DecimalField(max_digits=4, decimal_places=2,)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


