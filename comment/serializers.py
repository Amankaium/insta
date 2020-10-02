from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class CommentSerializer(ModelSerializer):
    likes = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = [
            "user", "publication",
            "text", "created",
            "likes"
        ]

    def get_likes(self, obj):
        return obj.like.count()


class CommentLikeSerializer(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ["user", "comment", "created"]


class CommentToCommentSerializer(ModelSerializer):
    likes = SerializerMethodField()
    
    class Meta:
        model = CommentToComment
        fields = [
            "user", "comment",
            "text", "created",
            "likes"
        ]

    def get_likes(self, obj):
        return obj.like.count()


class CommentToCommentLikeSerializer(ModelSerializer):
    class Meta:
        model = CommentToCommentLike
        fields = ["user", "comment", "created"]