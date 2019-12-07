from django.db import models

# Create your models here.
class ProductOwner(models.Model):
    id_customer = models.CharField(max_length=10)
    nik = models.CharField(max_length=20)
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    alamat = models.CharField(max_length=200)

class Product(models.Model):
    id_product = models.CharField(max_length=10)
    id_customer = models.ForeignKey(ProductOwner, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    kategori = models.IntegerField()
    deskripsi = models.CharField(max_length=500)
    harga = models.IntegerField()
    jumlah = models.IntegerField()
    foto = models.FileField(blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.id_product,self.nama)