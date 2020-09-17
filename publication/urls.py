from django.urls import path
from rest_framework import routers
from .views import PublicationViewSet

router = routers.DefaultRouter()
router.register(r"publication", PublicationViewSet)

# urlpattern = [
#     path("", VIEW, name)
# ]

# urlpatterns += router.urls

urlpatterns = router.urls
