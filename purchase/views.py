from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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


def purchasePlan(request):
    """ A view to buy a plan """

    form = ExtendedUserCreationForm()
    profileForm = UserProfileForm()

    context = {
        'form': form,
        'profileForm': profileForm,
    }

    return render(request, 'purchase/purchase_plan.html', context)


def signup(request):
    if request.method == 'POST':

        formData = ExtendedUserCreationForm(request.POST)
        profileForm = UserProfileForm(request.POST)

        context = {'form': formData, 'profileForm': profileForm}

        if formData.is_valid() and profileForm.is_valid():

            user = formData.save()
            plan = get_object_or_404(Plan, pk=request.POST.get("plan"))

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.plan = plan
            profile.save()

            username = formData.cleaned_data.get('username')
            password = formData.cleaned_data.get('password')

            return redirect("courses")

    return render(request, 'purchase/purchase_plan.html', context)
