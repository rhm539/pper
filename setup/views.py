from django.shortcuts import render
from django.http import HttpResponse
from setup.models import buyer, style


def buyer_list(request):
    Buyer = buyer.objects.all().order_by('name')
    context = {
        'Buyers': Buyer,
    }
    return render(request, 'setup/buyerList.html', context)


def weekly(request):
    return HttpResponse('Weekly Goals')


def monthly(request):
    return HttpResponse('Monthly Goals')


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
