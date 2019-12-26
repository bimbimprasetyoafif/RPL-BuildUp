from django.db import models

# Create your models here.
class Categorys(models.Model):
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.CategoryName

class CategorysHome(models.Model):
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.CategoryName