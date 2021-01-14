from django.db import models
from django.contrib.auth.models import User
from purchase.models import Plan
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, null=True, blank=True,
                             on_delete=models.SET_NULL, limit_choices_to={'active': True})
    date_joined = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(
        default="default-profile-picture.jpg", upload_to='profile_img')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
