# Generated by Django 2.1.7 on 2019-12-07 17:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191207_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id_customer',
            new_name='id_toko',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='productowner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='productowner',
            name='id',
        ),
        migrations.RemoveField(
            model_name='productowner',
            name='id_customer',
        ),
        migrations.RemoveField(
            model_name='productowner',
            name='nik',
        ),
        migrations.AddField(
            model_name='productowner',
            name='id_toko',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id_product',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
