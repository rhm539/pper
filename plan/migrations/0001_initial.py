# Generated by Django 4.1.2 on 2022-10-12 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setup', '0010_alter_buyer_created_at_alter_style_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleveryDate', models.DateField()),
                ('inputDate', models.DateField()),
                ('sewingEndDate', models.DateField()),
                ('orderQty', models.PositiveSmallIntegerField(default=0)),
                ('planQtyExtra', models.PositiveSmallIntegerField(default=0)),
                ('linePlanQty', models.PositiveSmallIntegerField(default=0)),
                ('estimateWorkDay', models.PositiveSmallIntegerField(default=0)),
                ('DataLock', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('modified', models.DateField(auto_now=True)),
                ('Line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.line')),
                ('Style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.style')),
                ('Unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.unit')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
