from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from setup.forms import *
from setup.models import buyer, style
from django.contrib import messages


def buyer_list(request):
    Buyer = buyer.objects.all().order_by('name')
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
    }
    return render(request, 'setup/buyerListAdd.html', context)


def buyer_edit(request, pk):
    Buyer = buyer.objects.all().order_by('name')
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
        'form': form,
        'pk': pk,
    }
    return render(request, 'setup/buyerListEdit.html', context)


def style_list(request):
    Style = style.objects.all()
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
    }
    return render(request, 'setup/styleListAdd.html', context)


def style_edit(request, pk):
    Style = style.objects.all().order_by('name')
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
