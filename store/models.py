from django.db import models

# Create your models here.
class Stores(models.Model):
    StoreId= models.AutoField(primary_key=True, editable=False, unique=True,)
    StoreName = models.CharField(max_length=50)
    StoreAddress = models.CharField(max_length=500)
    StoreImage = models.FileField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.StoreId,self.StoreName)