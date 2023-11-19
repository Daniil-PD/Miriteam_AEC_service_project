# Generated by Django 4.2.7 on 2023-11-19 00:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('vector', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
    ]