from django.db import models
from django.utils import timezone

# Create your models here.
holiday = (
    ('6', 'Sunday'),
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
)


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class userType(models.Model):
    typeName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.typeName}'


class unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    shortcut = models.CharField(max_length=6, unique=True)
    address = models.CharField(max_length=100)
    holiday = models.CharField(max_length=1, choices=holiday)
    startDuty = models.PositiveSmallIntegerField(null=True, default=8)
    endDuty = models.PositiveSmallIntegerField(null=True, default=17)

    def __str__(self):
        return f'{self.name}'


class buyer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    shortcut = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=100)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class style(models.Model):
    name = models.CharField(max_length=50, unique=True)
    buyer = models.ForeignKey(buyer, models.CASCADE, null=True)
    smv = models.DecimalField(max_digits=5, decimal_places=3)
    created_at = models.DateField(default=timezone.now)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class floor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    unit = models.ForeignKey(unit, models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'


class line(models.Model):
    name = models.CharField(max_length=50, unique=True)
    floor = models.ForeignKey(floor, models.CASCADE, null=True)
    unit = models.ForeignKey(unit, models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'
