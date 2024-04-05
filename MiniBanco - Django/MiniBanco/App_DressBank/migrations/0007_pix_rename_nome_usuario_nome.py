# Generated by Django 5.0.3 on 2024-03-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_DressBank', '0006_rename_cpf_usuario_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField()),
                ('hora', models.IntegerField()),
                ('origem', models.TextField(max_length=30)),
                ('destinovalor', models.TextField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Nome',
            new_name='nome',
        ),
    ]