# Generated by Django 5.0.3 on 2024-03-27 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_DressBank', '0016_rename_pix_pagamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamentos',
            name='dia',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='pagamentos',
            name='hora',
            field=models.IntegerField(default=1),
        ),
    ]