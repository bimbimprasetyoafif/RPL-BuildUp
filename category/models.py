from django.db import models

# Create your models here.
class Categorys(models.Model):
    categoryId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.categoryId, self.categoryName)

class CategorysHome(models.Model):
    categoryId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.categoryId, self.categoryName)