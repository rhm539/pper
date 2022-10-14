
from django.db import models
from setup.models import *
from plan.models import *
# Create your models here.


class production(models.Model):
    sewingDate = models.DateField()
    unit = models.ForeignKey(unit, models.CASCADE, null=True)
    planID = models.CharField(max_length=150, null=True)
    plan = models.ForeignKey(plan, models.CASCADE, null=True)
    #LineNum = models.ForeignKey(ProLine, models.CASCADE, null=True)
    #style= models.ForeignKey(Style, models.CASCADE, null=True)
    #HourTerget = models.PositiveSmallIntegerField(default=0)
    #DayTT = models.PositiveSmallIntegerField(default=0)
    workHour = models.PositiveSmallIntegerField(default=10)
    dayTerget = models.PositiveSmallIntegerField(default=0)
    hourTerget = models.PositiveSmallIntegerField(default=0)
    LineWIP = models.PositiveSmallIntegerField(default=0, blank=True)
    operator = models.PositiveSmallIntegerField(default=0, blank=True)
    helper = models.PositiveSmallIntegerField(default=0, blank=True)
    H_8_9 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_9_10 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_10_11 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_11_12 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_12_13 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_14_15 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_15_16 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_16_17 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_17_18 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_18_19 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_19_20 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_20_21 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_21_22 = models.PositiveSmallIntegerField(default=0, blank=True)
    #
    dataLock = models.BooleanField(default=False)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    created_at = models.DateField(default=timezone.now)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.sewingDate}'
