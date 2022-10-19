from django.shortcuts import render
from datetime import date, datetime
from django.shortcuts import redirect, render
from plan.forms import planAddForms
from plan.views import Plan_layout_day, findOutDate, unitKnow
from production.forms import productionHourForm
from django.contrib import messages
from production.models import production


# Create your views here.


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


def hourly_report_entry(request, Data):
    Data
    print('rob')
    return Data


def hourly_report_entry_plan(request, pk):
    productionData = production.objects.get(pk=pk)
    mydate = productionData.sewingDate
    if request.method == 'POST':
        form = productionHourForm(request.POST, instance=productionData)
        if form.is_valid():
            Data = form.save(commit=False)
            #Data = hourly_report_entry(Data)
            Data.save()
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
            #Data = hourly_report_entry(Data)
            Data.save()
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
