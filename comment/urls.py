from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'comment', CommentViewSet, basename="comment")
router.register(r'comment-like', CommentLikeViewSet, basename="comment-like")
router.register(r'comment-to-comment', CommentToCommentViewSet, basename="comment-to-comment")
router.register(r'comment-to-comment-like', CommentToCommentLikeViewSet, basename="comment-to-comment-like")

urlpatterns = router.urls



