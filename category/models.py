from django.db import models

# Create your models here.
class Categorys(models.Model):
    CategoryId= models.AutoField(primary_key=True, editable=False, unique=True,)
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.CategoryId,self.CategoryName)

class CategorysHome(models.Model):
    CategoryId= models.AutoField(primary_key=True, editable=False, unique=True,)
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.CategoryId,self.CategoryName)