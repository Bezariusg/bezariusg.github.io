# Generated by Django 3.2.4 on 2021-06-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0002_auto_20210605_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacciones',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
