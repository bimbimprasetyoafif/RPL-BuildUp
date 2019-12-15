from django.db import models
from category.models import Categorys
from store.models import Stores

# Create your models here.
class Products(models.Model):
    ProductId = models.IntegerField(primary_key=True)
    ProductCategory = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    StoreId = models.ForeignKey(Stores,related_name='ProductItems', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=50)
    ProductDesc = models.CharField(max_length=500)
    ProductPrice = models.IntegerField()
    ProductStock = models.IntegerField()
    ProductSatuan = models.IntegerField()
    ProductNamaSatuan = models.CharField(max_length=20)
    ProductImage = models.FileField(blank=False, null=False)
    
    def __str__(self):
        return "{} - {}".format(self.ProductId,self.ProductName)