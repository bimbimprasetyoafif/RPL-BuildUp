from django.db import models
from django.conf import settings
from category.models import CategorysHome
# Create your models here.

class Design(models.Model):
    designId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    category = models.ForeignKey(CategorysHome, related_name="designInCategory", on_delete=models.CASCADE)
    designName = models.CharField(max_length=50)
    designDesc = models.CharField(max_length=500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='allDesign', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.designName, self.creator)

class RAB(models.Model):
    rabId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="allRAB", on_delete=models.CASCADE,)
    workName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.workName, self.priceTotal)

class MaterialAtap(models.Model):
    materialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="customAtap", on_delete=models.CASCADE,)
    materialName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.materialName, self.priceTotal)

class MaterialPlafon(models.Model):
    materialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="customPlafon", on_delete=models.CASCADE,)
    materialName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.materialName, self.priceTotal)

class MaterialDinding(models.Model):
    materialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="customDinding", on_delete=models.CASCADE,)
    materialName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.materialName, self.priceTotal)

class MaterialLantai(models.Model):
    materialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="customLantai", on_delete=models.CASCADE,)
    materialName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.materialName, self.priceTotal)

class MaterialCatLuar(models.Model):
    materialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="customCatLuar", on_delete=models.CASCADE,)
    materialName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.materialName, self.priceTotal)

class MaterialCatDalam(models.Model):
    materialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    designId = models.ForeignKey(Design, related_name="customCatDalam", on_delete=models.CASCADE,)
    materialName = models.CharField(max_length=50)
    priceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.designId, self.materialName, self.priceTotal)

class DesignImages(models.Model):
    designId = models.ForeignKey(Design, related_name="allImagesDesign", on_delete=models.CASCADE,)
    Image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.designId, self.Image)