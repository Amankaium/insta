from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, \
    ListAPIView, UpdateAPIView
from .serializers import *
from .models import Profile


class ProfileRetrieveView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    # lookup_field = "user__username"
    queryset = Profile.objects.all()


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.filter(is_active=True)


class SubscribingListView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        user = User.objects.get(username=username)
        lst = user.profile.subscription.filter(is_active=True)
        return lst


class SubscribersListView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        lst = User.objects.filter(profile__subscription__in=[user])
        return lst


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileEditSerializer
    queryset = Profile.objects.all()


class ProfileUpdate(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()


class UserUpdate(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
 

