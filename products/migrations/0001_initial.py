# Generated by Django 2.1.7 on 2019-12-15 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductId', models.IntegerField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=50)),
                ('ProductDesc', models.CharField(max_length=500)),
                ('ProductPrice', models.IntegerField()),
                ('ProductStock', models.IntegerField()),
                ('ProductSatuan', models.IntegerField()),
                ('ProductNamaSatuan', models.CharField(max_length=20)),
                ('ProductImage', models.FileField(upload_to='')),
                ('ProductCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Categorys')),
            ],
        ),
    ]
