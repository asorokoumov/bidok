from django.contrib import admin

# Register your models here.
from .models import Order, Bid

admin.site.register(Order)
admin.site.register(Bid)