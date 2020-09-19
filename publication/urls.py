from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"publication", PublicationViewSet)

urlpatterns = [
    path("detail/<int:pk>/", publication)
]

urlpatterns += router.urls

# urlpatterns = router.urls
