from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
# Create your views here.


@login_required
def getUserProfile(request, user_id):
    """ A view to show all lessons within a course """

    userProfile = get_object_or_404(UserProfile, user_id=user_id)

    context = {
        'userProfile': userProfile,
    }

    return render(request, 'profiles/user_profile.html', context)
