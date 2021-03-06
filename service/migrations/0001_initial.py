# Generated by Django 3.2.9 on 2021-11-26 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PriceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=100)),
                ('validity', models.CharField(choices=[('day', 'day'), ('month', 'month'), ('year', 'year')], max_length=100)),
                ('contains', models.TextField(max_length=2000)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.packagetypemodel')),
            ],
        ),
    ]
