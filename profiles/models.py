from django.db import models
from django.contrib.auth.models import User
from purchase.models import Plan


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username
