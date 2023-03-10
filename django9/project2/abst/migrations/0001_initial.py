# Generated by Django 3.2.14 on 2022-07-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ntstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('doj', models.DateField(auto_now_add=True)),
                ('quali', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('doj', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=30)),
                ('fee', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('doj', models.DateField(auto_now_add=True)),
                ('quali', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('course', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
