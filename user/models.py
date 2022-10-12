from django.db import models

from django.contrib.auth.models import User

from setup.models import *

# Create your models here.


class Profile(models.Model):
    loginuser = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    officeID = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, models.CASCADE, null=True)
    unit = models.ForeignKey(unit, models.CASCADE, null=True)
    utype = models.ForeignKey(userType, models.CASCADE, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(default='pdefault.png',
                              upload_to='profile_images', blank=True, null=True)
    signature = models.ImageField(
        default='sdefault.png', upload_to='signature_images', blank=True, null=True)

    def __str__(self):
        return f'{self.loginuser.username}-Profile'
