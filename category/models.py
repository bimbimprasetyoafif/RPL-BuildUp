from django.db import models

# Create your models here.
class Categorys(models.Model):
    CategoryId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.CategoryId, self.CategoryName)

class CategorysHome(models.Model):
    CategoryId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.CategoryId, self.CategoryName)