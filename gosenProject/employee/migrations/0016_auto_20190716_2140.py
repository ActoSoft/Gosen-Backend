# Generated by Django 2.2.2 on 2019-07-17 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20190716_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contracted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to='Admin.Admin'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fired_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firer', to='Admin.Admin'),
        ),
    ]
