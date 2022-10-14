from django.shortcuts import render

from setup.models import line

# Create your views here.


def index(request, unit):
    unitline = line.objects.all().filter(unit=unit)
    context = {
        'line': unitline,
        'unit': unit,
    }
    return render(request, 'dashboard/index.html', context)
