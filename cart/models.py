from django.db import models
from django.conf import settings
from allUsers.models import Account
from products.models import Products

# Create your models here.
class Cart(models.Model):
    CartId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    CustomerId = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Cart', on_delete=models.CASCADE)
    productId = models.ForeignKey(Products,related_name="InCart" ,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.CustomerId, self.productId)

