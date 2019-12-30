from django.db import models
from django.conf import settings
from category.models import CategorysHome
# Create your models here.

class Design(models.Model):
    DesignId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    category = models.ForeignKey(CategorysHome, related_name="DesignInCategory", on_delete=models.CASCADE)
    DesignName = models.CharField(max_length=50)
    DesignDesc = models.CharField(max_length=500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='allDesign', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.DesignName, self.creator)

class RAB(models.Model):
    RABId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="allRAB", on_delete=models.CASCADE,)
    WorkName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.WorkName, self.PriceTotal)

class MaterialAtap(models.Model):
    MaterialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="CustomAtap", on_delete=models.CASCADE,)
    MaterialName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.MaterialName, self.PriceTotal)

class MaterialPlafon(models.Model):
    MaterialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="CustomPlafon", on_delete=models.CASCADE,)
    MaterialName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.MaterialName, self.PriceTotal)

class MaterialDinding(models.Model):
    MaterialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="CustomDinding", on_delete=models.CASCADE,)
    MaterialName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.MaterialName, self.PriceTotal)

class MaterialLantai(models.Model):
    MaterialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="CustomLantai", on_delete=models.CASCADE,)
    MaterialName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.MaterialName, self.PriceTotal)

class MaterialCatLuar(models.Model):
    MaterialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="CustomCatLuar", on_delete=models.CASCADE,)
    MaterialName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.MaterialName, self.PriceTotal)

class MaterialCatDalam(models.Model):
    MaterialId = models.AutoField(auto_created=True, primary_key=True, editable=False)
    DesignId = models.ForeignKey(Design, related_name="CustomCatDalam", on_delete=models.CASCADE,)
    MaterialName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.DesignId, self.MaterialName, self.PriceTotal)

class DesignImages(models.Model):
    DesignId = models.ForeignKey(Design, related_name="allImagesDesign", on_delete=models.CASCADE,)
    Image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.DesignId, self.Image)