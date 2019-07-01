from django.contrib import admin

# Register your models here.
from .models import Order, Bid

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class BidAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Order, OrderAdmin)
admin.site.register(Bid, BidAdmin)

