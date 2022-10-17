# Generated by Django 4.1.2 on 2022-10-12 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0004_buyer_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 12, 12, 55, 17, 396772)),
        ),
        migrations.AddField(
            model_name='style',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 12, 12, 55, 17, 396461)),
        ),
    ]