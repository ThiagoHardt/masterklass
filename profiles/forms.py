from django import forms
from django.contrib.auth.models import User
from profiles.models import UserProfile


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ["username", "email"]


class UpdateUserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ["name", "profile_picture"]
