# Generated by Django 2.2.2 on 2019-07-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('cost', models.CharField(blank=True, max_length=150, null=True)),
                ('payment_tipe', models.CharField(choices=[('semanal', 'Semanal'), ('quincenal', 'Quincenal'), ('mensual', 'Mensual')], default='Quincenal', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
