# Generated by Django 4.1.2 on 2022-10-13 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0011_alter_unit_holiday'),
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='Buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.buyer'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='planQtyExtra',
            field=models.PositiveSmallIntegerField(default=3),
        ),
    ]