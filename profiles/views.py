from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateUserProfileForm


@login_required
def profile(request):
    """ A view to view and edit user profiles """

    if request.method == 'POST':

        userForm = UpdateUserForm(request.POST, instance=request.user)
        profileForm = UpdateUserProfileForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if userForm.is_valid() and profileForm.is_valid():

            userForm.save()
            profileForm.save()
            message = "Profile updated successfully."
            messages.success(request, message)

            return redirect("profile")
    else:
        userForm = UpdateUserForm(instance=request.user)
        profileForm = UpdateUserProfileForm(instance=request.user.userprofile)

    context = {
        "userForm": userForm,
        "profileForm": profileForm,
    }

    return render(request, 'profiles/user_profile.html', context)
