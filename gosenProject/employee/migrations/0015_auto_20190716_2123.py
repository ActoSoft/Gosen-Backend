# Generated by Django 2.2.2 on 2019-07-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_auto_20190716_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contract_date_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fired_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]