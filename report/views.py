from django.db.models import Sum
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from plan.views import unitKnow
from plan.views import Plan_layout_day, findOutDate
from production.views import EfficiencyCaculator
from setup.models import floor, unit
#
from django.template.loader import get_template
from django.core.mail import EmailMessage
# Create your views here.


def UnitReportCalculation(productionData):
    Line_dayTarget_smv = 0
    Line_dayTarget = 0
    Line_workHour = 0
    Line_manpower = 0
    Line_workHourAEFF = 0
    Line_manpowerAEFF = 0
    Line_OutputAEFF = 0

    unit_Average_SMV = 0
    unit_targetEfficiency = 0
    unit_achievementEfficiency = 0

    for lineProduction in productionData:
        if lineProduction.targetEfficiency > 0 and lineProduction.style.smv > 0:
            Line_dayTarget_smv = (lineProduction.dayTarget *
                                  float(lineProduction.style.smv))+Line_dayTarget_smv
            Line_dayTarget = lineProduction.dayTarget + Line_dayTarget
            Line_workHour = Line_workHour+lineProduction.workHour
            Line_manpower = Line_manpower+lineProduction.manpower
        if lineProduction.achievementEfficiency > 0:
            Line_manpowerAEFF = Line_manpowerAEFF+lineProduction.manpower
            Line_workHourAEFF = Line_workHourAEFF+lineProduction.workHour
            Line_OutputAEFF = Line_OutputAEFF+lineProduction.dayAchievement
    if Line_dayTarget > 0:
        unit_Average_SMV = Line_dayTarget_smv/Line_dayTarget

    unitProduction = productionData.aggregate(manpower=Sum('manpower'), operator=Sum('operator'), helper=Sum('helper'), workHour=Sum('workHour'), dayTarget=Sum('dayTarget'), hourTarget=Sum('hourTarget'), dayAchievement=Sum('dayAchievement'), vari=Sum('vari'), LineWIP=Sum('LineWIP'), H_8_9=Sum(
        'H_8_9'), H_9_10=Sum('H_9_10'), H_10_11=Sum('H_10_11'), H_11_12=Sum('H_11_12'), H_12_13=Sum('H_12_13'), H_14_15=Sum('H_14_15'), H_15_16=Sum('H_15_16'), H_16_17=Sum('H_16_17'), H_17_18=Sum('H_17_18'), H_18_19=Sum('H_18_19'), H_19_20=Sum('H_19_20'), H_20_21=Sum('H_20_21'), H_21_22=Sum('H_21_22'),)
    if Line_manpower > 0 and Line_workHour > 0:
        unit_targetEfficiency = EfficiencyCaculator(
            Line_dayTarget, unit_Average_SMV, Line_manpower, Line_workHour)
    if Line_manpowerAEFF > 0 and Line_workHourAEFF > 0:
        unit_achievementEfficiency = EfficiencyCaculator(
            Line_OutputAEFF, unit_Average_SMV, Line_manpowerAEFF, Line_workHourAEFF)
    return unitProduction, unit_Average_SMV, unit_targetEfficiency, unit_achievementEfficiency


def FloorAverageSMV(floors, productionData):
    floorProduction = productionData.filter(floor__name=floors)
    Line_dayTarget_smv = 0
    Line_dayTarget = 0
    Line_workHour = 0
    Line_manpower = 0
    Line_workHourAEFF = 0
    Line_manpowerAEFF = 0
    Line_OutputAEFF = 0
    Floor_Average_SMV = 0
    Floor_targetEfficiency = 0
    Floor_achievementEfficiency = 0
    for lineProduction in floorProduction:
        if lineProduction.targetEfficiency > 0 and lineProduction.style.smv > 0:
            Line_dayTarget_smv = (lineProduction.dayTarget *
                                  float(lineProduction.style.smv))+Line_dayTarget_smv
            Line_dayTarget = lineProduction.dayTarget + Line_dayTarget
            Line_workHour = Line_workHour+lineProduction.workHour
            Line_manpower = Line_manpower+lineProduction.manpower
        if lineProduction.achievementEfficiency > 0:
            Line_manpowerAEFF = Line_manpowerAEFF+lineProduction.manpower
            Line_workHourAEFF = Line_workHourAEFF+lineProduction.workHour
            Line_OutputAEFF = Line_OutputAEFF+lineProduction.dayAchievement
    if Line_dayTarget > 0 and Line_dayTarget_smv > 0 and Line_OutputAEFF > 0 and Line_manpowerAEFF > 0:
        Floor_Average_SMV = Line_dayTarget_smv/Line_dayTarget
        Floor_targetEfficiency = EfficiencyCaculator(
            Line_dayTarget, Floor_Average_SMV, Line_manpower, Line_workHour)
        Floor_achievementEfficiency = EfficiencyCaculator(
            Line_OutputAEFF, Floor_Average_SMV, Line_manpowerAEFF, Line_workHourAEFF)
    return Floor_Average_SMV, Floor_targetEfficiency, Floor_achievementEfficiency


def FloorReportCalculation(productionData, unit):
    floorData = floor.objects.filter(unit=unit)
    floorList = []
    Average_SMV = []
    targetEfficiency = []
    achievementEfficiency = []
    for floors in floorData:
        Floor_Average_SMV, Floor_targetEfficiency, Floor_achievementEfficiency = FloorAverageSMV(
            floors, productionData)
        floorGroup = productionData.filter(floor__name=floors).aggregate(manpower=Sum('manpower'), operator=Sum('operator'), helper=Sum('helper'), workHour=Sum('workHour'), dayTarget=Sum('dayTarget'), hourTarget=Sum('hourTarget'), dayAchievement=Sum('dayAchievement'), vari=Sum('vari'), LineWIP=Sum(
            'LineWIP'), H_8_9=Sum('H_8_9'), H_9_10=Sum('H_9_10'), H_10_11=Sum('H_10_11'), H_11_12=Sum('H_11_12'), H_12_13=Sum('H_12_13'), H_14_15=Sum('H_14_15'), H_15_16=Sum('H_15_16'), H_16_17=Sum('H_16_17'), H_17_18=Sum('H_17_18'), H_18_19=Sum('H_18_19'), H_19_20=Sum('H_19_20'), H_20_21=Sum('H_20_21'), H_21_22=Sum('H_21_22'),)
        floorList.append(floorGroup)
        Average_SMV.append(Floor_Average_SMV)
        targetEfficiency.append(Floor_targetEfficiency)
        achievementEfficiency.append(Floor_achievementEfficiency)
    #unitSmv = UnitAverageSMV(productionData)
    zippedList = zip(floorList, floorData, Average_SMV,
                     targetEfficiency, achievementEfficiency)
    return zippedList, floorList, floorData


def report(mydate, units):
    unitData = unit.objects.get(pk=units)
    lastDay, curentDay, nextDay = findOutDate(mydate)
    productionData = Plan_layout_day(units, mydate)
    productionData = productionData.order_by('plan__line')
    zippedList, floorList, floorData = FloorReportCalculation(
        productionData, units)
    unitProduction, unit_Average_SMV, unit_targetEfficiency, unit_achievementEfficiency = UnitReportCalculation(
        productionData)
    goToPage = 'report-day-production-nav'

    context = {
        'unit_targetEfficiency': unit_targetEfficiency,
        'unit_achievementEfficiency': unit_achievementEfficiency,
        'unitSmv': unit_Average_SMV,
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
        'unit': units,
        'unitData': unitData,

    }
    return context


def report_day_production_nav(request, mydate, unit):
    context = report(mydate, unit)
    return render(request, 'report/report_day_production.html', context)


def report_day_production(request, unit):
    mydate = date.today()
    context = report(mydate, unit)
    #message = get_template('report/report_day_production.html').render(context)
    return render(request, 'report/report_day_production.html', context)


@login_required
def report_mail(request, mydate):
    unit = unitKnow(request)
    context = report(mydate, unit.id)
    message = get_template('report/mail.html').render(context)
    if unit.shortcut == 'BRL':
        mailGo1 = 'a.rob@fashionstepbd.net'
        mailGo2 = 'auto_ie_brl@fashionstepbd.net'
    elif unit.shortcut == 'FSL':
        mailGo1 = 'a.rob@fashionstepbd.net'
        mailGo2 = 'auto_ie_fsl@fashionstepbd.net'

    msg = EmailMessage(
        'Subject: Daily Production Report',
        message,
        'project@fashionstepbd.net',
        [mailGo1, mailGo2],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return redirect('report-day-production', unit.id)
    # return render(request, 'report/mail.html', context)


'''
    message = get_template('report/mail.html').render(context)
    msg = EmailMessage(
        'Subject: Fund Requisition',
        message,
        'project@fashionstepbd.net',
        ['a.rob@fashionstepbd.net'],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return redirect('report-day-production', unit.id)
'''


def report_mail_view(request, mydate):
    unit = unitKnow(request)
    context = report(mydate, unit.id)
    return render(request, 'report/mail.html', context)
