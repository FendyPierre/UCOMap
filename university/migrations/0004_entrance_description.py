# Generated by Django 3.2.7 on 2021-09-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_alter_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrance',
            name='description',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
