# Generated by Django 2.2.2 on 2019-09-23 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='stocks',
        ),
    ]
