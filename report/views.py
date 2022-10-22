from django.db.models import Sum
from datetime import date
from itertools import product
from django.shortcuts import render

from plan.views import Plan_layout_day, findOutDate, unitKnow
from production.models import production
from setup.models import floor

# Create your views here.


def report_calculation(productionData, unit):
    floorData = floor.objects.filter(unit=unit)
    floorList = []
    for floors in floorData:
        floorGroup = productionData.filter(floor__name=floors).aggregate(manpower=Sum('manpower'), operator=Sum('operator'), helper=Sum('helper'), workHour=Sum('workHour'), dayTarget=Sum('dayTarget'), hourTarget=Sum('hourTarget'), dayAchievement=Sum('dayAchievement'), vari=Sum('vari'), LineWIP=Sum(
            'LineWIP'), H_8_9=Sum('H_8_9'), H_9_10=Sum('H_9_10'), H_10_11=Sum('H_10_11'), H_11_12=Sum('H_11_12'), H_12_13=Sum('H_12_13'), H_14_15=Sum('H_14_15'), H_15_16=Sum('H_15_16'), H_16_17=Sum('H_16_17'), H_17_18=Sum('H_17_18'), H_18_19=Sum('H_18_19'), H_19_20=Sum('H_19_20'), H_20_21=Sum('H_20_21'), H_21_22=Sum('H_21_22'),)
        floorList.append(floorGroup)
    unitProduction = productionData.aggregate(manpower=Sum('manpower'), operator=Sum('operator'), helper=Sum('helper'), workHour=Sum('workHour'), dayTarget=Sum('dayTarget'), hourTarget=Sum('hourTarget'), dayAchievement=Sum('dayAchievement'), vari=Sum('vari'), LineWIP=Sum('LineWIP'), H_8_9=Sum(
        'H_8_9'), H_9_10=Sum('H_9_10'), H_10_11=Sum('H_10_11'), H_11_12=Sum('H_11_12'), H_12_13=Sum('H_12_13'), H_14_15=Sum('H_14_15'), H_15_16=Sum('H_15_16'), H_16_17=Sum('H_16_17'), H_17_18=Sum('H_17_18'), H_18_19=Sum('H_18_19'), H_19_20=Sum('H_19_20'), H_20_21=Sum('H_20_21'), H_21_22=Sum('H_21_22'),)
    zippedList = zip(floorList, floorData)
    return zippedList, floorList, floorData, unitProduction


def report_day_production_nav(request, mydate, unit):
    lastDay, curentDay, nextDay = findOutDate(mydate)
    productionData = Plan_layout_day(unit, mydate)
    productionData = productionData.order_by('plan__line')
    zippedList, floorList, floorData, unitProduction = report_calculation(
        productionData, unit)
    goToPage = 'report-day-production-nav'
    context = {
        'unitProduction': unitProduction,
        'list': zippedList,
        'floorList': floorList,
        'floorData': floorData,
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
        'unit': unit,
    }
    return render(request, 'report/report_day_production.html', context)


def report_day_production(request, unit):
    mydate = date.today()
    lastDay, curentDay, nextDay = findOutDate(mydate)
    productionData = Plan_layout_day(unit, mydate)
    productionData = productionData.order_by('plan__line')
    zippedList, floorList, floorData, unitProduction = report_calculation(
        productionData, unit)
    goToPage = 'report-day-production-nav'
    context = {
        'unitProduction': unitProduction,
        'list': zippedList,
        'floorList': floorList,
        'floorData': floorData,
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
        'unit': unit,
    }
    return render(request, 'report/report_day_production.html', context)
