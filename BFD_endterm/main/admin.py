from django.contrib import admin
from .models import FoodCategory, FoodItem, CreditCard, Order, ShoppingCart

admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(CreditCard)
admin.site.register(ShoppingCart)
admin.site.register(Order)
