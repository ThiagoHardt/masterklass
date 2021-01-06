from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):

    """ User profile model """

    plan_type = models.SlugField(max_length=255)

    def __str__(self):
        return self.username
