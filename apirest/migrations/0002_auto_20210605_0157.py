# Generated by Django 3.2.4 on 2021-06-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacciones',
            name='debe',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='transacciones',
            name='haber',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='transacciones',
            name='id_transaccion',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
    ]
