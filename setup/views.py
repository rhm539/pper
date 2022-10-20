import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from setup.forms import *
from setup.models import buyer, style
from django.contrib import messages
from datetime import date, timedelta
from django.db.models import Q


def dateFind():
    toDay = date.today()
    last7Day = toDay - timedelta(days=45)
    date7Range = Q(created_at__range=[last7Day, toDay])
    return date7Range


def buyerStatus():
    date7Range = dateFind()
    Buyer = buyer.objects.all().order_by('name')
    totalBuyer = Buyer.count()
    newBuyer = Buyer.filter(date7Range).count()
    return Buyer, newBuyer, totalBuyer


def styleStatus():
    date7Range = dateFind()
    Style = style.objects.all().order_by('-created_at')
    totalStyle = Style.count()
    newStyle = Style.filter(date7Range).count()
    return Style, newStyle, totalStyle


'''
def date_default():
    enddate = date.today()
    startdate = enddate - timedelta(days=45)
    dateQ = Q(date__range=[startdate, enddate])
    return dateQ


def date_enddate(enddate):
    if not enddate:
        enddate = date.today()
    else:
        enddate = datetime.strptime(enddate, "%m/%d/%Y").strftime('%Y-%m-%d')
    return enddate


def date_startdate(startdate):
    if not startdate:
        startdate = '2021-06-01'
    else:
        startdate = datetime.strptime(
            startdate, "%m/%d/%Y").strftime('%Y-%m-%d')
    return startdate
'''


def buyer_list(request):
    Buyer, newBuyer, totalBuyer = buyerStatus()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BuyerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form)
            # return HttpResponseRedirect('buyer-list')
            form.save()
            messages.success(request, 'Successful, Buyer Add in PPER System')
            return redirect('buyer-list')
        else:
            form = BuyerForm()
            messages.warning(
                request, 'Unsuccessful, Buyer Cannot Add in PPER System')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BuyerForm()
    context = {
        'Buyers': Buyer,
        'form': form,
        'totalBuyer': totalBuyer,
        'newBuyer': newBuyer,
    }
    return render(request, 'setup/buyerListAdd.html', context)


def buyer_edit(request, pk):
    Buyer, newBuyer, totalBuyer = buyerStatus()
    BuyerEdit = buyer.objects.get(id=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BuyerForm(request.POST, instance=BuyerEdit)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form)
            # return HttpResponseRedirect('buyer-list')
            form.save()
            messages.success(request, 'Successful, Buyer Add in PPER System')
            return redirect('buyer-list')
        else:
            messages.warning(
                request, 'Unsuccessful, Buyer Cannot Add in PPER System')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BuyerForm(instance=BuyerEdit)
    context = {
        'Buyers': Buyer,
        'totalBuyer': totalBuyer,
        'newBuyer': newBuyer,
        'form': form,
        'pk': pk,
    }
    return render(request, 'setup/buyerListEdit.html', context)


def style_list(request):
    Style, newStyle, totalStyle = styleStatus()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StyleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form)
            # return HttpResponseRedirect('buyer-list')
            form.save()
            messages.success(request, 'Successful, Style Add in PPER System')
            return redirect('style-list')
        else:
            form = StyleForm()
            messages.warning(
                request, 'Unsuccessful, Style Cannot Add in PPER System')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = StyleForm()
    context = {
        'Style': Style,
        'form': form,
        'newStyle': newStyle,
        'totalStyle': totalStyle,
    }
    return render(request, 'setup/styleListAdd.html', context)


def style_edit(request, pk):
    Style, newStyle, totalStyle = styleStatus()
    StyleEdit = style.objects.get(id=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StyleForm(request.POST, instance=StyleEdit)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form)
            # return HttpResponseRedirect('buyer-list')
            form.save()
            messages.success(request, 'Successful, Style Add in PPER System')
            return redirect('style-list')
        else:
            messages.warning(
                request, 'Unsuccessful, Buyer Cannot Add in PPER System')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = StyleForm(instance=StyleEdit)
    context = {
        'Style': Style,
        'form': form,
        'pk': pk,
        'newStyle': newStyle,
        'totalStyle': totalStyle,
    }
    return render(request, 'setup/styleListEdit.html', context)


'''
def buyer_edit(request, pk):
    Buyer = buyer.objects.all().order_by('name')
    BuyerEdit = buyer.objects.get(id=pk)
    form = BuyerForm()
    context = {
        'Buyers': Buyer,
        'form': form,
    }
    return render(request, 'setup/buyerList.html', context)

'''
'''
    def buyerlist(request):
    clientDATA = Buyer.objects.all().order_by('name')
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fslplan-buyer-list')
    else:
        form = BuyerForm()
    context = {
        'form': form,
        'clientDATA': clientDATA,
    }
    return render(request, 'fslplan/buyer_list.html', context)
'''
