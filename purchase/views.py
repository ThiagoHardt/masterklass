from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Plan
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.password_validation import validate_password
from .forms import ExtendedUserCreationForm, UserProfileForm
import stripe


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

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=int(plan.price)*100,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'form': form,
        'profileForm': profileForm,
        'plan': plan,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'purchase/purchase_plan.html', context)


def signup(request):
    """ Create a user if payment is successful """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        formData = ExtendedUserCreationForm(request.POST)
        plan = Plan.objects.get(pk=request.POST.get('planId'))
        profileForm = UserProfileForm(request.POST)
        stripe.api_key = stripe_secret_key

        context = {
            'form': formData,
            'profileForm': profileForm,
            'plan': plan,
            'stripe_public_key': stripe_public_key,
        }

        if formData.is_valid() and profileForm.is_valid():

            user = formData.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.plan = plan
            profile.save()

            logout(request)
            message = "Account created successfully, please login."
            messages.success(request, message)
            return redirect("account_login")

    return render(request, 'purchase/purchase_plan.html', context)


def preValidadeUser(request):

    username = request.GET.get('username', None)
    email = request.GET.get('email', None)
    password1 = request.GET.get('password1', None)
    password2 = request.GET.get('password2', None)
    passwordMatch = False

    if (password1 == password2):
        passwordMatch = True

    data = {
        'usernameNotValid': User.objects.filter(username__iexact=username).exists(),
        'emailNotValid': User.objects.filter(email__iexact=email).exists(),
        'passwordMatch': passwordMatch,
    }
    return JsonResponse(data)
