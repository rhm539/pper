from django.db import models
from setup.models import *
from plan.models import *
# Create your models here.
datastatus = (
    ('Y', 'YES'),
    ('N', 'NO'),
)


class production(models.Model):
    sewingDate = models.DateField()
    unit = models.ForeignKey(unit, models.CASCADE, null=True)
    planID = models.CharField(max_length=150, null=True)
    plan = models.ForeignKey(plan, models.CASCADE, null=True)
    #LineNum = models.ForeignKey(ProLine, models.CASCADE, null=True)
    #style= models.ForeignKey(Style, models.CASCADE, null=True)
    #HourTerget = models.PositiveSmallIntegerField(default=0)
    #DayTT = models.PositiveSmallIntegerField(default=0)
    manpower = models.PositiveSmallIntegerField(default=0, blank=True)
    operator = models.PositiveSmallIntegerField(default=0, blank=True)
    helper = models.PositiveSmallIntegerField(default=0, blank=True)
    runDay = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    dotHour = models.PositiveSmallIntegerField(default=0, blank=True)
    workHour = models.PositiveSmallIntegerField(default=10)
    dayTarget = models.PositiveSmallIntegerField(default=0)
    hourTarget = models.PositiveSmallIntegerField(default=0)
    dayAchievement = models.PositiveSmallIntegerField(default=0, blank=True)
    targetEfficiency = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    achievementEfficiency = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    vari = models.PositiveSmallIntegerField(default=0, blank=True)
    LineWIP = models.PositiveSmallIntegerField(default=0, blank=True)
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
    totalProduction = models.PositiveSmallIntegerField(default=0, blank=True)
    #
    dataLock = models.CharField(
        max_length=2, default='N', choices=datastatus, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    created_at = models.DateField(default=timezone.now)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.sewingDate}'
