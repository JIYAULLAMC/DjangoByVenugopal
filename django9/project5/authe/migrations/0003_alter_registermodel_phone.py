# Generated by Django 4.0.6 on 2022-08-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0002_alter_registermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='phone',
            field=models.PositiveBigIntegerField(),
        ),
    ]
