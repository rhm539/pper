# Generated by Django 4.1.2 on 2022-10-11 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_alter_buyer_name_alter_buyer_shortcut_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.unit')),
            ],
        ),
        migrations.CreateModel(
            name='line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.floor')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.unit')),
            ],
        ),
    ]
