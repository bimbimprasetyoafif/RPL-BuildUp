from django.db import models

# Create your models here.
class Vendors(models.Model):
    VendorId= models.AutoField(primary_key=True, editable=False, unique=True,)
    VendorName = models.CharField(max_length=50)
    VendorAddress = models.CharField(max_length=500)
    VendorDesc = models.CharField(max_length=100)
    VendorImage = models.FileField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.VendorId,self.VendorName)