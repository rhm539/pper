from datetime import date
from itertools import product
from django.shortcuts import render

from plan.views import Plan_layout_day, findOutDate, unitKnow
from production.models import production
from setup.models import floor

# Create your views here.


def report_day_production_nav(request, mydate, unit):
    lastDay, curentDay, nextDay = findOutDate(mydate)
    productionData = Plan_layout_day(unit, mydate)

    goToPage = 'report-day-production-nav'
    context = {
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
    goToPage = 'report-day-production-nav'
    context = {
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
        'unit': unit,
    }
    return render(request, 'report/report_day_production.html', context)
