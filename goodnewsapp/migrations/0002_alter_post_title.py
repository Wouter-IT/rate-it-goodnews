# Generated by Django 3.2.23 on 2023-12-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodnewsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
