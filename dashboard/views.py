from django.shortcuts import render

from setup.models import line

# Create your views here.


def index(request):
    Line = line.objects.all()
    context = {
        'Line': Line,
    }
    return render(request, 'dashboard/index.html', context)
