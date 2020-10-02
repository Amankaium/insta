from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentLikeViewSet(ModelViewSet):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()


class CommentToCommentViewSet(ModelViewSet):
    serializer_class = CommentToCommentSerializer
    queryset = CommentToComment.objects.all()


class CommentToCommentLikeViewSet(ModelViewSet):
    serializer_class = CommentToCommentLikeSerializer
    queryset = CommentToCommentLike.objects.all()
