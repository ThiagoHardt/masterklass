from django.shortcuts import render, get_object_or_404
from .models import Plan
from .forms import SignupForm

# Create your views here.


def plans(request):
    """ A view to show all plans available """
    plans = Plan.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'purchase/plans.html', context)


def purchasePlan(request, id):
    """ A view to buy a plan and signup to the service """

    plan = get_object_or_404(Plan, pk=id)
    signupForm = SignupForm()

    context = {
        'signupForm': signupForm,
        'plan': plan,
    }

    return render(request, 'purchase/purchase_plan.html', context)


def signup(request):
    if request.method == 'POST':
        formData = {
            "username": request.POST["username"],
            "email": request.POST["email"]
        }

    signupForm = SignupForm(formData)
    # if signupForm.is_valid():

    return render(request, "home/index.html")
