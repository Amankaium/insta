from django.urls import path
from .views import *



urlpatterns = [
    # path("<username>/", ProfileRetrieveView.as_view(), name="profile"),
    path("<username>/", UserRetrieveView.as_view(), name="get-user"),
    path("<username>/following/", SubscribingListView.as_view(), name='subscribing-list'),
    path("<username>/followers/", SubscribersListView.as_view())
]