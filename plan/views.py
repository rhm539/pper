from datetime import date, timedelta
from django.shortcuts import render
from django.contrib import messages
from plan.forms import PlanForm
from django.shortcuts import render, redirect
from production.models import production

from setup.models import buyer, style, line
# Create your views here.

# AJAX


def percentageToAmount(amount, percentage):
    amountValue = round(((amount*percentage)/100)+amount)
    # print(amountValue)
    return amountValue


def planDate(deleveryDate, inputDate, sewingEndDate):
    toDay = date.today()
    datePass = False
    nextDay = toDay + timedelta(days=180)
    peviousDay = toDay - timedelta(days=14)
    if inputDate < nextDay and inputDate > peviousDay:
        datePass = True
    else:
        datePass = False
    if sewingEndDate < nextDay and sewingEndDate > peviousDay and sewingEndDate >= inputDate:
        datePass = True
    else:
        datePass = False
    if deleveryDate < nextDay and deleveryDate > peviousDay:
        if deleveryDate >= inputDate and deleveryDate >= sewingEndDate:
            datePass = True
        else:
            datePass = False
    else:
        datePass = False
    return datePass


def planBook(inputDate, sewingEndDate):

    planForDay = sewingEndDate - inputDate
    planForDay = (planForDay.days)+1
    return planForDay


def load_style(request):
    buyer = request.GET.get('buyer')
    styles = style.objects.filter(buyer=buyer).all()
    return render(request, 'plan/style_load.html', {'styles': styles})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def planEntry(request, pk):
    lineData = line.objects.get(pk=pk)
    weekend = lineData.unit.holiday
    # print(weekend)
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            planData = form.save(commit=False)
            datePass = planDate(planData.deleveryDate,
                                planData.inputDate, planData.sewingEndDate)
            if planData.orderQty > 0 and datePass is True:
                planForDay = planBook(planData.inputDate,
                                      planData.sewingEndDate)
                sewingDate = planData.inputDate
                planData.unit = lineData.unit
                planData.line = lineData
                planData.planQtyExtra = percentageToAmount(
                    planData.orderQty, planData.planQtyExtra)
                planData.staff = request.user
                planData.save()
                for x in range(planForDay):
                    dayName = sewingDate.weekday()
                    if int(weekend) != int(dayName):
                        productionPlan = production()
                        productionPlan.sewingDate = sewingDate
                        productionPlan.unit = lineData.unit
                        productionPlan.planID = planData.planID
                        productionPlan.plan = planData
                        productionPlan.staff = request.user
                        productionPlan.save()
                    sewingDate += timedelta(days=1)
                messages.success(
                    request, 'Successful, Plan Add in PPER System')
                return redirect('buyer-list')
            else:
                messages.warning(
                    request, 'Unsuccessful, Order Quy. Cannot Zero and check Date')
        else:
            form = PlanForm()
            messages.warning(
                request, 'Unsuccessful, Plan Cannot Add in PPER System')
    else:
        form = PlanForm()
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'plan/planEntry.html', context)
