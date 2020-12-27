from django.shortcuts import render
from .models import Plan

# Create your views here.


def plans(request):
    """ A view to show all plans available """
    plans = Plan.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'purchase/plans.html', context)
