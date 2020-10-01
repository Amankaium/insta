from django.contrib import admin
from .models import *


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "description",
        "publisher",
        "likes",
        "created",
        "updated",
        "deleted"
    ]

    fields = [
        "image",
        "description",
        "publisher",
        "likes",
    ]

    def likes(self, obj):
        return obj.like.count()

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "publication_count",
        "created"
    ]

    def publication_count(self, obj):
        return obj.publication.count()

admin.site.register(Like)