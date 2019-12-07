from django.contrib import admin
from .models import Product, ProductOwner
# Register your models here

admin.site.register(Product)
admin.site.register(ProductOwner)