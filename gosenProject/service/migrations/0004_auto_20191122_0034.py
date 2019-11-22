# Generated by Django 2.2.2 on 2019-11-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20190716_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='payment_type',
            field=models.CharField(choices=[('hora', 'Hora'), ('dia', 'Dia'), ('semanal', 'Semanal'), ('quincenal', 'Quincenal'), ('mensual', 'Mensual'), ('bimestral', 'Bimestral'), ('trimestral', 'Trimestral'), ('semestral', 'Semestral'), ('anual', 'Anual')], default='quincenal', max_length=100),
        ),
    ]