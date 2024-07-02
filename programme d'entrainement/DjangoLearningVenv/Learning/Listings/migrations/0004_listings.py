# Generated by Django 5.0.1 on 2024-01-28 01:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0003_remove_band_title_band_active_band_biography_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('description', models.TextField(default='', max_length='255')),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('type', models.CharField(choices=[('rc', 'Records'), ('Ct', 'Clothing'), ('Pt', 'Posters'), ('Mn', 'Miscellaneous')], max_length=5)),
            ],
        ),
    ]
