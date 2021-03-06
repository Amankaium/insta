from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "user",
        "created",
        "updated",
        "deleted"
    ]

    # fields = ["user", "subscription"]
    exclude = ["name", "deleted"]