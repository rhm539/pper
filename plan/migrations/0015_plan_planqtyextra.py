# Generated by Django 4.1.2 on 2022-10-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0014_alter_plan_totalorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='planQtyExtra',
            field=models.PositiveSmallIntegerField(default=3),
        ),
    ]
