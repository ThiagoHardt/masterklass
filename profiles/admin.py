from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "plan",
        "date_joined",
        "active",
    )

    readonly_fields = ('date_joined',)
    ordering = ("date_joined",)


admin.site.register(UserProfile, UserProfileAdmin)
