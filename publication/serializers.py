from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *

class PublicationSerializer(ModelSerializer):
    likes = SerializerMethodField()

    class Meta:
        model = Publication
        fields = [
            "pk", "image", "description",
            "publisher", "created",
            "likes"
        ]

    def get_likes(self, obj):
        return obj.like.count()


class PublicationListSerializer(ModelSerializer):
    likes = SerializerMethodField()

    class Meta:
        model = Publication
        fields = [
            "pk",
            "image",
            "likes",
            # "comments"
        ]
    
    def get_likes(self, obj):
        return obj.like.count()


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "publication", "created"]