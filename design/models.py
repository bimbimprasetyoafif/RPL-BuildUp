from django.db import models
from django.conf import settings
from category.models import CategorysHome
# Create your models here.

class Design(models.Model):
    category = models.ForeignKey(CategorysHome, related_name="DesignInCategory", on_delete=models.CASCADE)
    DesignName = models.CharField(max_length=50)
    DesignDesc = models.CharField(max_length=500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='allDesign', on_delete=models.CASCADE, null=True, blank=True)

class RAB(models.Model):
    WorkName = models.CharField(max_length=50)
    PriceTotal = models.IntegerField()

class DesignImages(models.Model):
    DesignId = models.ForeignKey(Design, related_name="allImagesDesign", on_delete=models.CASCADE,)
    Image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.DesignId, self.Image)