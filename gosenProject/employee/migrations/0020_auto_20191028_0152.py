# Generated by Django 2.2.2 on 2019-10-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_auto_20191028_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='payment_type',
            field=models.CharField(choices=[('hora', 'Hora'), ('dia', 'Dia'), ('semanal', 'Semanal'), ('quincenal', 'Quincenal'), ('mensual', 'Mensual'), ('bimestral', 'Bimestral'), ('trimestral', 'Trimestral'), ('semestral', 'Semestral'), ('anual', 'Anual')], default='Quincenal', max_length=100),
        ),
    ]
