# Generated by Django 3.2.6 on 2021-09-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
