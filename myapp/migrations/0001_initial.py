# Generated by Django 4.0.2 on 2022-04-20 00:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jyl', models.CharField(max_length=200)),
                ('soz', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Eltanba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jyl', models.CharField(max_length=15)),
                ('aty', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Qoldan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Numbers not allowed.')])),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('confirm', models.CharField(max_length=255)),
                ('em_pass', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ramiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aty', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('to_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
