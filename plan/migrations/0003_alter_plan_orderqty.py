# Generated by Django 4.1.2 on 2022-10-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_plan_buyer_alter_plan_planqtyextra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='orderQty',
            field=models.IntegerField(default=0),
        ),
    ]
