from django.db import models


# Create your models here.
class Order (models.Model):
    number = models.TextField(default=None, blank=True, null=True)
    address_from = models.TextField(default=None, blank=True, null=True)
    address_to = models.TextField(default=None, blank=True, null=True)
    rate = models.FloatField(default=None, blank=True, null=True)
    distance = models.FloatField(default=None, blank=True, null=True)
    pickup_date = models.DateField(default=None, blank=True, null=True)
    weight = models.FloatField(default=None, blank=True, null=True)
    car_type = models.TextField(default=None, blank=True, null=True)
    cargo_type = models.TextField(default=None, blank=True, null=True)
    cargo_count = models.FloatField(default=None, blank=True, null=True)
    price = models.FloatField(default=None, blank=True, null=True)
    map = models.TextField(default=None, blank=True, null=True)
    comment = models.TextField(default=None, blank=True, null=True)
    logist = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class Bid (models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.TextField(default=None, blank=True, null=True)
    phone = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id.number