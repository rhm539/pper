from pyexpat import model
from django.db import models

# Create your models here.


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

    def __str__(self):
        return f'{self.name}'


class buyer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    shortcut = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class style(models.Model):
    name = models.CharField(max_length=50, unique=True)
    buyer = models.ForeignKey(buyer, models.CASCADE, null=True)
    smv = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return f'{self.name}'
