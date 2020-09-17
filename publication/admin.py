from django.contrib import admin
from .models import *


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "description",
        "publisher",
        "created",
        "updated",
        "deleted"
    ]

    fields = [
        "image",
        "description",
        "publisher",
    ]



