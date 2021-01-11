from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Plan
from .forms import ExtendedUserCreationForm, UserProfileForm


# Create your views here.


def plans(request):
    """ A view to show all plans available """
    plans = Plan.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'purchase/plans.html', context)


def purchasePlan(request, plan_id):
    """ A view to buy a plan """
    plan = Plan.objects.get(pk=plan_id)
    form = ExtendedUserCreationForm()
    profileForm = UserProfileForm()

    context = {
        'form': form,
        'profileForm': profileForm,
        'plan': plan,
        'stripe_public_key': 'pk_test_51HxBfnEz5cJqldVxRK4MUQHAaBJlUJOy911vphGfdlxBFkVaCtP2LjQIJCvPm1udTClUwwte7du2vSODhWds5Tr600Br24qJe6',
    }

    return render(request, 'purchase/purchase_plan.html', context)


def signup(request):
    if request.method == 'POST':

        formData = ExtendedUserCreationForm(request.POST)
        plan = Plan.objects.get(pk=request.POST.get('planId'))
        profileForm = UserProfileForm(request.POST)

        context = {'form': formData, 'profileForm': profileForm, 'plan': plan}

        if formData.is_valid() and profileForm.is_valid():

            user = formData.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.plan = plan
            profile.save()

            logout(request)

            return redirect("account_login")

    return render(request, 'purchase/purchase_plan.html', context)
