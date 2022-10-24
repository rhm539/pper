
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.contrib import messages
from plan.forms import PlanForm, planAddForms
from django.shortcuts import render, redirect
from plan.models import plan
from production.models import production
from django.forms import modelformset_factory


from setup.models import style, line
# Create your views here.

# ((Output*SMV)/(Manpower*(Working*60)))*100


def EfficiencyCaculator(Output, SMV, Manpower, WorkingHour):
    if float(SMV) > 0 and Manpower > 0 and WorkingHour > 0 and Output > 0:
        Efficiency = ((Output*SMV)/(Manpower*(WorkingHour*60))) * 100
    return Efficiency


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)


def unitKnow(request):
    unitKnow = request.user.profile.unit
    return unitKnow


def findOutDate(anyDay):
    curentDay = curentDay = date.today()
    nextDay = anyDay + timedelta(days=1)
    lastDay = anyDay - timedelta(days=1)
    return lastDay, curentDay, nextDay

# percentage To Amount 3% 103


def percentageToAmount(amount, percentage):
    amountValue = round(((amount*percentage)/100)+amount)
    # print(amountValue)
    return amountValue

# date check of plan from


def planDate(deleveryDate, sewingStartDate, sewingEndDate):
    toDay = date.today()
    datePass = False
    nextDay = toDay + timedelta(days=180)
    peviousDay = toDay - timedelta(days=14)
    if sewingStartDate < nextDay and sewingStartDate > peviousDay:
        datePass = True
    else:
        datePass = False
    if sewingEndDate < nextDay and sewingEndDate > peviousDay and sewingEndDate >= sewingStartDate:
        datePass = True
    else:
        datePass = False
    if deleveryDate < nextDay and deleveryDate > peviousDay:
        if deleveryDate >= sewingStartDate and deleveryDate >= sewingEndDate:
            datePass = True
        else:
            datePass = False
    else:
        datePass = False
    return datePass

# finout amoun of day


def planBook(sewingStartDate, sewingEndDate):
    planForDay = sewingEndDate - sewingStartDate
    planForDay = (planForDay.days)+1
    return planForDay

# depandency drop down menu


def load_style(request):
    buyer = request.GET.get('buyer')
    styles = style.objects.filter(buyer=buyer).all()
    return render(request, 'plan/style_load.html', {'styles': styles})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


@login_required
def planEntry(request, pk):
    lineData = line.objects.get(pk=pk)
    weekend = lineData.unit.holiday
    # print(weekend)
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            planData = form.save(commit=False)
            datePass = planDate(planData.deleveryDate,
                                planData.sewingStartDate, planData.sewingEndDate)
            if planData.orderQty > 0 and datePass is True:
                planForDay = planBook(planData.sewingStartDate,
                                      planData.sewingEndDate)
                sewingDate = planData.sewingStartDate
                planData.unit = lineData.unit
                planData.line = lineData
                planData.totalOrder = percentageToAmount(
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
                        productionPlan.style = planData.style
                        productionPlan.line = planData.line
                        productionPlan.floor = planData.line.floor
                        productionPlan.staff = request.user
                        productionPlan.save()
                    sewingDate += timedelta(days=1)
                messages.success(
                    request, 'Successful, Plan Add in PPER System')
                return redirect('plan-Entry-show', planData.pk)
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
        'lineName': lineData.name,
    }
    return render(request, 'plan/planEntry.html', context)


def planEdit(request, pk):
    #lineData = line.objects.get(pk=pk)
    planData = plan.objects.get(id=pk)
    productionData = production.objects.filter(plan=pk, dataLock='N')
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=planData)
        if form.is_valid():
            planData = form.save(commit=False)
            datePass = planDate(planData.deleveryDate,
                                planData.sewingStartDate, planData.sewingEndDate)
            if planData.orderQty > 0 and planData.planQtyExtra < 10 and datePass is True:
                planData.totalOrder = percentageToAmount(
                    planData.orderQty, planData.planQtyExtra)
                planData.buyer = planData.style.buyer
                planData.staff = request.user
                planData.save()
                for productions in productionData:
                    productions.style = planData.style
                    productions.save()
                messages.success(
                    request, 'Successful, Plan Update in PPER System')
                return redirect('plan-Entry-show', planData.pk)
            else:
                form = PlanForm(instance=planData)
                messages.warning(
                    request, 'unsuccessful, please set 3 Qty.Extra field')
    else:
        form = PlanForm(instance=planData)
    context = {
        'form': form,
        'pk': pk,
<<<<<<< HEAD
        'lineName': planData.line.name,
=======

>>>>>>> a0e64ace5c01fb93e1a00661ae433a3e39cd7406
    }
    return render(request, 'plan/planEdit.html', context)


def plan_Entry_show(request, pk):
    planSummary = plan.objects.get(pk=pk)
    planDetail = production.objects.filter(plan=pk).order_by('sewingDate')
    context = {
        'planSummary': planSummary,
        'planDetail': planDetail,

    }
    return render(request, 'plan/planEntryShow.html', context)


def linePlan_show(request, pk):
    planSummary = plan.objects.all().filter(line=pk).order_by('sewingStartDate')
    context = {
        'planSummary': planSummary,
        # 'planDetail': planDetail,
    }
    return render(request, 'plan/linePlanShow.html', context)


def forcast_table(request):
    pk = request.user.profile.unit
    planSummary = plan.objects.all().filter(unit=pk).order_by('sewingStartDate')
    context = {
        'planSummary': planSummary,
        # 'planDetail': planDetail,
    }
    return render(request, 'plan/linePlanShow.html', context)


'''


def Plan_layout(request):

    context = {

    }
    return render(request, 'plan/plan_layout.html', context)


'''


def Plan_layout_day(unit, dateData):
    productionData = production.objects.filter(
        sewingDate=dateData, unit__id=unit).order_by('line')
    return productionData


def Plan_layout_nav(request, mydate):
    unit = unitKnow(request)
    lastDay, curentDay, nextDay = findOutDate(mydate)
    productionData = Plan_layout_day(unit.id, mydate)
    goToPage = 'Plan-Layout-nav'
    context = {
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
    }
    return render(request, 'plan/plan_layout.html', context)


def Plan_layout(request):
    unit = unitKnow(request)
    mydate = date.today()
    lastDay, curentDay, nextDay = findOutDate(mydate)
    goToPage = 'Plan-Layout-nav'
    productionData = Plan_layout_day(unit.id, mydate)
    context = {
        'production': productionData,
        'lastDay': lastDay,
        'curentDay': curentDay,
        'nextDay': nextDay,
        'goToPage': goToPage,
        'mydate': mydate,
    }
    return render(request, 'plan/plan_layout.html', context)


def plan_line_lock(request, pk):
    productionData = production.objects.get(pk=pk)
    mydate = productionData.sewingDate
    if productionData.dataLock == 'Y':
        productionData.dataLock = 'N'
        # productionData.save()
        # return redirect('plan-Entry-show', productionData.plan)
    else:
        productionData.dataLock = 'Y'
    productionData.save()
    return redirect('Plan-Layout-nav', mydate)


def plan_line_move(request, pk):
    productionData = production.objects.get(pk=pk)
    weekend = productionData.unit.holiday
    mydate = productionData.sewingDate
    planData = plan.objects.get(pk=productionData.plan.id)
    anyDay = planData.sewingEndDate
    lastDay, curentDay, nextDay = findOutDate(anyDay)
    dayName = nextDay.weekday()
    if int(weekend) != int(dayName):
        productionData.sewingDate = nextDay
        planData.sewingEndDate = nextDay
        planData.save()
        productionData.save()
    else:
        lastDay, curentDay, nextDay = findOutDate(nextDay)
        productionData.sewingDate = nextDay
        planData.sewingEndDate = nextDay
        planData.save()
        productionData.save()
    return redirect('Plan-Layout-nav', mydate)


def add_plan(request, mydate):
    unit = unitKnow(request)
    productionData = production.objects.filter(
        sewingDate=mydate, dataLock='N', unit=unit).order_by('line')
    planFormSet = modelformset_factory(production, planAddForms, extra=0)
    if request.method == 'POST':
        formset = planFormSet(request.POST)
        if formset.is_valid():
            addPlanData = formset.save(commit=False)
            for addPlan in addPlanData:
                planData = plan.objects.get(pk=addPlan.plan.id)
<<<<<<< HEAD
                if addPlan.workHour > 0 and addPlan.dayTarget > 0 and addPlan.style.smv > 0:
=======
                if addPlan.workHour > 0:
>>>>>>> a0e64ace5c01fb93e1a00661ae433a3e39cd7406
                    addPlan.line = planData.line
                    addPlan.style = planData.style
                    addPlan.manpower = addPlan.operator+addPlan.helper
                    addPlan.hourTarget = round(
                        addPlan.dayTarget / addPlan.workHour)
                    if addPlan.manpower > 0 and addPlan.style.smv > 0:
                        addPlan.targetEfficiency = EfficiencyCaculator(addPlan.dayTarget, float(
                            addPlan.style.smv), addPlan.manpower, addPlan.workHour)
                    addPlan.save()
                # return redirect('add-plan', mydate)
            return redirect('Plan-Layout-nav', mydate)
    else:
        formset = planFormSet(queryset=productionData)
    context = {
        'formset': formset,
        'mydate': mydate,
        'productionData': productionData,
    }
    return render(request, 'plan/add_plan.html', context)
