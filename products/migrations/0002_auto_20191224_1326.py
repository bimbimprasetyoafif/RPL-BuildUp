# Generated by Django 2.1.7 on 2019-12-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='ProductImage',
            field=models.ImageField(upload_to=''),
        ),
    ]
