import uuid
from django.db import models

# Create your models here.
class ProductOwner(models.Model):
    id_toko = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.id_toko,self.nama)

class Product(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_toko = models.ForeignKey(ProductOwner, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    kategori = models.IntegerField()
    deskripsi = models.CharField(max_length=500)
    harga = models.IntegerField()
    jumlah = models.IntegerField()
    foto = models.FileField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.id_product,self.nama)