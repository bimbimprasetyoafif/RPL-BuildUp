# Generated by Django 2.1.7 on 2019-12-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorysHome',
            fields=[
                ('CategoryId', models.IntegerField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=50)),
            ],
        ),
    ]
