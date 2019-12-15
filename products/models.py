from django.db import models
from category.models import Categorys

# Create your models here.
class Products(models.Model):
    ProductId = models.IntegerField(primary_key=True)
    ProductCategory = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=50)
    ProductDesc = models.CharField(max_length=500)
    ProductPrice = models.IntegerField()
    ProductStock = models.IntegerField()
    ProductSatuan = models.IntegerField()
    ProductNamaSatuan = models.CharField(max_length=20)
    ProductImage = models.FileField(blank=False, null=False)
    
    