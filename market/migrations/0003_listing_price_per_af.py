# Generated by Django 2.1 on 2018-11-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20181104_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price_per_af',
            field=models.IntegerField(default=0),
        ),
    ]
