# Generated by Django 4.0.5 on 2022-07-27 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('iid', models.BigAutoField(primary_key=True, serialize=False)),
                ('iname', models.CharField(max_length=50)),
                ('iprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pid', models.BigAutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pprice', models.IntegerField()),
                ('pdesc', models.TextField()),
                ('iid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.itemmodel')),
            ],
        ),
    ]
