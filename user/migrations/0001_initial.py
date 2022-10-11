# Generated by Django 4.1.2 on 2022-10-11 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setup', '0002_alter_buyer_name_alter_buyer_shortcut_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('officeID', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(default='pdefault.png', upload_to='profile_images')),
                ('signature', models.ImageField(default='sdefault.png', upload_to='signature_images')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.department')),
                ('loginuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('utype', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.usertype')),
            ],
        ),
    ]