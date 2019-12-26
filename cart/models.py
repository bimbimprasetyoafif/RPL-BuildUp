from django.db import models
from allUsers.models import Account
from products.models import Products

# Create your models here.
class Cart(models.Model):
    cartId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    CustomerId = models.ForeignKey(Account, related_name="InCart", on_delete=models.CASCADE)
    productId = models.ForeignKey(Products,related_name="InCart" ,on_delete=models.CASCADE)
    quantity = models.IntegerField()

