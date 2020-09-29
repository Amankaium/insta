from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"publication", PublicationViewSet)

urlpatterns = [
    path("detail/<int:pk>/", publication),
    path("<username>/", UserPublicationList.as_view()),
    path("<username>/feed/", FeedList.as_view()),
    path("<username>/explore/", ExploreView.as_view())
]

urlpatterns += router.urls

# urlpatterns = router.urls
