# Generated by Django 5.0.3 on 2024-03-27 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_DressBank', '0012_alter_usuario_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='saldo',
            field=models.FloatField(default=0),
        ),
    ]
