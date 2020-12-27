from django.shortcuts import render

# Create your views here.


def plans(request):
    """ A view to show all plans available """
    context = {

    }
    return render(request, 'purchase/plans.html', context)
