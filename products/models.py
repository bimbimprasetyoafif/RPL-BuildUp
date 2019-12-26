from django.db import models
from django.conf import settings
from category.models import Categorys

# Create your models here.
class Products(models.Model):
    ProductCategory = models.ForeignKey(Categorys,related_name='ProductInCategory', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=50)
    ProductDesc = models.CharField(max_length=500)
    ProductPrice = models.IntegerField()
    ProductStock = models.IntegerField()
    ProductSatuan = models.IntegerField()
    ProductNamaSatuan = models.CharField(max_length=20)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='allProduct', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.creator,self.ProductName)

class ProductImages(models.Model):
    ProdId = models.ForeignKey(Products, related_name="allImagesProduct", on_delete=models.CASCADE,)
    ProductImage = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.ProdId, self.ProductImage.name)