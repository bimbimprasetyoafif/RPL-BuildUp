from django.db import models
from django.conf import settings
from category.models import Categorys
from store.models import Stores

# Create your models here.
class Products(models.Model):
    ProductId = models.AutoField(primary_key=True, editable=False, unique=True,)
    ProductCategory = models.ForeignKey(Categorys,related_name='ProductInCategory', on_delete=models.CASCADE)
    StoreId = models.ForeignKey(Stores,related_name='ProductItems', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=50)
    ProductDesc = models.CharField(max_length=500)
    ProductPrice = models.IntegerField()
    ProductStock = models.IntegerField()
    ProductSatuan = models.IntegerField()
    ProductNamaSatuan = models.CharField(max_length=20)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.ProductId,self.ProductName)

class ProductImages(models.Model):
    ProdId = models.ForeignKey(Products, related_name="ImagesProduct", on_delete=models.CASCADE,)
    ProductImage = models.FileField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.ProdId, self.ProductImage.name)