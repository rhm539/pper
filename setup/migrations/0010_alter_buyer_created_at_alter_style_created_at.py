# Generated by Django 4.1.2 on 2022-10-12 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0009_alter_buyer_created_at_alter_style_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='style',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
