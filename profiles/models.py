from django.db import models
from django.contrib.auth.models import User
from purchase.models import Plan


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, null=True, blank=True,
                             on_delete=models.SET_NULL, limit_choices_to={'active': True})
    date_joined = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
