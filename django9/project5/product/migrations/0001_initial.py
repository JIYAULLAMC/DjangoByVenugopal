# Generated by Django 4.0.6 on 2022-08-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('pid', models.BigAutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pmodel', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('discount', models.PositiveSmallIntegerField()),
                ('pic', models.ImageField(upload_to='productpics/')),
            ],
        ),
    ]
