# Generated by Django 2.2.2 on 2019-11-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_client_zip_code'),
        ('employee', '0020_auto_20191028_0152'),
        ('service', '0004_auto_20191122_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payed', models.DecimalField(decimal_places=2, max_digits=8)),
                ('to_pay', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('in_progress', 'En Curso'), ('finished', 'Finalizado'), ('pending', 'Pendiente'), ('authorized', 'Autorizado'), ('canceled', 'Cancelado')], default='pending', max_length=20)),
                ('datetime_start', models.DateTimeField()),
                ('datetime_end', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='client.Client')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='service.Service')),
            ],
        ),
        migrations.CreateModel(
            name='WorkEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='employee.Employee')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='works.Work')),
            ],
        ),
    ]