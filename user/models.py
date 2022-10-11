from django.db import models

from django.contrib.auth.models import User

from setup.models import Department, userType

# Create your models here.


class Profile(models.Model):
    loginuser = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    officeID = models.CharField(max_length=20, null=False)
    designation = models.CharField(max_length=50, null=True)
    department = models.ForeignKey(Department, models.CASCADE, null=True)
    utype = models.ForeignKey(userType, models.CASCADE, null=True, default='1')
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    image = models.ImageField(default='pdefault.png',
                              upload_to='profile_images')
    signature = models.ImageField(
        default='sdefault.png', upload_to='signature_images')

    def __str__(self):
        return f'{self.loginuser.username}-Profile'
