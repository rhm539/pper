from django.shortcuts import render
from django.http import HttpResponse


def daily(request):
    return render(request,'setup/buyerAdd.html')


def weekly(request):
    return HttpResponse('Weekly Goals')


def monthly(request):
    return HttpResponse('Monthly Goals')