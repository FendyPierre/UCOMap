# Generated by Django 3.2.7 on 2021-09-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
