# Generated by Django 4.0.5 on 2022-07-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankmodel',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=40)),
                ('ifsc', models.CharField(max_length=20)),
            ],
        ),
    ]
