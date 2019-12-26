# Generated by Django 2.1.7 on 2019-12-26 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductImage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductId', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=50)),
                ('ProductDesc', models.CharField(max_length=500)),
                ('ProductPrice', models.IntegerField()),
                ('ProductStock', models.IntegerField()),
                ('ProductSatuan', models.IntegerField()),
                ('ProductNamaSatuan', models.CharField(max_length=20)),
                ('ProductCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductInCategory', to='category.Categorys')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allProduct', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='productimages',
            name='ProdId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allImagesProduct', to='products.Products'),
        ),
    ]
