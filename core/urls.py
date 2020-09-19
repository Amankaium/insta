from django.urls import path
from .views import *



urlpatterns = [
    path("<int:pk>/", ProfileRetrieveView.as_view(), name="profile"),
]