from django.shortcuts import render
from datetime import date, datetime
from django.shortcuts import redirect, render
from plan.forms import planAddForms
from plan.models import plan
from plan.views import Plan_layout_day, findOutDate, unitKnow
from production.forms import productionHourForm
from django.contrib import messages
from production.models import production


# Create your views here.

# ((Output*SMV)/(Manpower*(Working*60)))*100
def EfficiencyCaculator(Output, SMV, Manpower, Working):
    Efficiency = ((Output*SMV)/(Manpower*(Working*60))) * 100
    return Efficiency


def line_layout_nev(request, mydate):
    unit = unitKnow(request)
    lastDay, curentDay, nextDay = findOutDate(mydate)
    productionData = Plan_layout_day(unit, mydate)
    goToPage = 'line-Layout-nav'
    context = {
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
    }
    return render(request, 'production/line_layout.html', context)


def line_layout(request):
    unit = unitKnow(request)
    mydate = date.today()
    lastDay, curentDay, nextDay = findOutDate(mydate)
    goToPage = 'line-Layout-nav'
    productionData = Plan_layout_day(unit, mydate)
    context = {
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
    }
    return render(request, 'production/line_layout.html', context)


def hourly_report_entry(Data):
    dayAchievement = Data.H_8_9+Data.H_9_10+Data.H_10_11+Data.H_11_12+Data.H_12_13+Data.H_14_15 + \
        Data.H_15_16+Data.H_16_17+Data.H_17_18+Data.H_18_19 + \
        Data.H_19_20+Data.H_20_21+Data.H_21_22

    Data.dayAchievement = dayAchievement
    if Data.dayTarget > dayAchievement:
        Data.vari = Data.dayTarget - dayAchievement
    else:
        Data.vari = 0
    if Data.dayTarget > 0 and Data.style.smv > 0 and Data.manpower > 0 and Data.workHour > 0:
        Data.targetEfficiency = EfficiencyCaculator(
            Data.dayTarget, Data.style.smv, Data.manpower, Data.workHour)

        Data.achievementEfficiency = EfficiencyCaculator(
            Data.dayAchievement, Data.style.smv, Data.manpower, Data.workHour)

    Data.save()

    return None


def hourly_report_entry_plan(request, pk):
    productionData = production.objects.get(pk=pk)
    mydate = productionData.sewingDate
    if request.method == 'POST':
        form = productionHourForm(request.POST, instance=productionData)
        if form.is_valid():
            Data = form.save(commit=False)
            Data = hourly_report_entry(Data)
            # Data.save()
            messages.success(request, 'Successful, Buyer Add in PPER System')
            return redirect('line-Layout-nav', mydate)
    else:
        form = productionHourForm(instance=productionData)
    context = {
        'form': form,
        'production': productionData,
    }
    return render(request, 'production/hourly_report_entry_plan.html', context)


def hourly_report_entry_detail(request, pk):
    productionData = production.objects.get(pk=pk)
    mydate = productionData.sewingDate
    if request.method == 'POST':
        form = productionHourForm(request.POST, instance=productionData)
        if form.is_valid():
            Data = form.save(commit=False)
            Data = hourly_report_entry(Data)
            # Data.save()
            messages.success(request, 'Successful, Buyer Add in PPER System')
            return redirect('plan-Entry-show', productionData.plan.id)

    else:
        form = productionHourForm(instance=productionData)
    context = {
        'form': form,
        'production': productionData,
    }
    return render(request, 'production/hourly_report_entry_detail.html', context)


def line_delete(request, pk):
    productionData = production.objects.get(pk=pk)
    plan = production.objects.filter(plan=productionData.plan)
    pk = productionData.plan
    lineCount = plan.count()
    if productionData.totalProduction == 0:
        if lineCount > 1:
            productionData.delete()
            messages.warning(
                request, 'Unsuccessful, Line Delete in PPER System')
            return redirect('plan-Entry-show', pk)
        else:
            productionData.delete()
            plan.delete()
            messages.warning(
                request, 'Unsuccessful, Line and Plan Delete in PPER System')
            return redirect('forcast-table')
    else:
        messages.info(
            request, 'Unsuccessful, Line Cannot Delete in PPER System')
        return redirect('plan-Entry-show', pk)


def line_lock(request, pk):
    productionData = production.objects.get(pk=pk)
    if productionData.dataLock == 'Y':
        productionData.dataLock = 'N'
        # productionData.save()
        # return redirect('plan-Entry-show', productionData.plan)
    else:
        productionData.dataLock = 'Y'
    productionData.save()
    return redirect('plan-Entry-show', productionData.plan)


def line_add(request, pk):
    planData = plan.objects.get(pk=pk)
    #productionData = production.objects.get(plan=planData.id)
    weekend = planData.unit.holiday
    anyDay = planData.sewingEndDate
    lastDay, curentDay, nextDay = findOutDate(anyDay)
    dayName = nextDay.weekday()
    if int(weekend) != int(dayName):
        productionData = production()
        productionData.sewingDate = nextDay
        productionData.unit = planData.unit
        productionData.plan = planData
        productionData.planID = planData.planID
        productionData.style = planData.style
        productionData.line = planData.line
        productionData.floor = planData.line.floor

        planData.sewingEndDate = nextDay
        planData.save()
        productionData.save()
    else:
        lastDay, curentDay, nextDay = findOutDate(nextDay)
        productionData = production()
        productionData.sewingDate = nextDay
        productionData.unit = planData.unit
        productionData.plan = planData
        productionData.planID = planData.planID
        productionData.style = planData.style
        productionData.line = planData.line
        productionData.floor = planData.line.floor

        planData.sewingEndDate = nextDay
        planData.save()
        productionData.save()
    messages.success(request, 'Successful,  Day Added in PPER System')
    return redirect('plan-Entry-show', planData.id)
