# Generated by Django 2.2.2 on 2019-09-23 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
        ('products', '0003_auto_20190922_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stocks',
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='products.Product')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stocks.Stock')),
            ],
        ),
    ]
