# Generated by Django 4.1.2 on 2022-10-14 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_production_planid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='DataLock',
            new_name='dataLock',
        ),
        migrations.RenameField(
            model_name='production',
            old_name='Unit',
            new_name='unit',
        ),
    ]