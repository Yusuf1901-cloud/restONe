# Generated by Django 4.2 on 2023-05-08 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductManager',
        ),
    ]
