# Generated by Django 5.1.2 on 2024-10-14 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('property_type', models.CharField(choices=[('HOUSE', 'Casa'), ('APARTMENT', 'Departamento'), ('OFFICE', 'Oficina'), ('LAND', 'Terreno')], max_length=10)),
                ('offer_type', models.CharField(choices=[('LEASE', 'Arriendo'), ('SELL', 'Venta')], max_length=8)),
                ('price', models.DecimalField(decimal_places=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('common_expenses', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('square_meters', models.DecimalField(decimal_places=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('bedrooms', models.PositiveSmallIntegerField()),
                ('bathrooms', models.PositiveSmallIntegerField()),
                ('has_parking', models.BooleanField(default=False)),
                ('has_storage_unit', models.BooleanField(default=False)),
                ('floor_number', models.IntegerField(blank=True, null=True)),
                ('amenities', models.TextField(blank=True)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('requirements', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('property_description', models.TextField()),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
    ]