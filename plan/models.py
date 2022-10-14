import datetime
from django.db import models
from django.utils import timezone
from setup.models import *
from django.contrib.auth.models import User
# Create your models here.


def increment_booking_number():
    last_booking = plan.objects.all().order_by('planID').last()
    if not last_booking:
        return 'PLN' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000'
    booking_id = last_booking.planID
    booking_int = int(booking_id[11:14])
    new_booking_int = booking_int + 1
    new_booking_id = 'PLN' + str(str(datetime.date.today().year)) + str(datetime.date.today(
    ).month).zfill(2) + str(datetime.date.today().day).zfill(2) + str(new_booking_int).zfill(3)
    return new_booking_id


class plan(models.Model):
    planID = models.CharField(
        max_length=150, default=increment_booking_number, null=True, unique=True)
    unit = models.ForeignKey(unit, models.CASCADE, null=True)
    buyer = models.ForeignKey(buyer, models.CASCADE, null=True)
    style = models.ForeignKey(style, models.CASCADE, null=True)
    line = models.ForeignKey(line, models.CASCADE, null=True)
    deleveryDate = models.DateField()
    inputDate = models.DateField()
    sewingEndDate = models.DateField()
    orderQty = models.IntegerField()
    planQtyExtra = models.PositiveSmallIntegerField(default=3)
    linePlanQty = models.PositiveSmallIntegerField(default=0)
    estimateWorkDay = models.PositiveSmallIntegerField(default=0)
    #
    dataLock = models.BooleanField(default=False)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    created_at = models.DateField(default=timezone.now)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.pk}'
