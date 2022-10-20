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
'''
