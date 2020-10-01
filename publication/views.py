from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.generics import ListAPIView, GenericAPIView
from requests import get

from .models import *
from .serializers import *


class PublicationViewSet(ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()


@api_view()
def publication(request, pk):
    if Publication.objects.filter(pk=pk).exists():
        pub = Publication.objects.get(pk=pk)
    else:
        return Response({"message": "Not found"}, HTTP_404_NOT_FOUND)
    serializer = PublicationSerializer(pub)
    # response = get("https://api.openweathermap.org/data/2.5/weather?q=Bishkek,kgz&appid=11c0d3dc6093f7442898ee49d2430d20")
    # response_data = response.json()
    data = serializer.data
    # data["temp"] = response_data["main"]["temp"] - 273.15
    return Response(data)


class UserPublicationList(ListAPIView):
    serializer_class = PublicationListSerializer
    # lookup_field = "username"
    
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs["username"])
        publications = Publication.objects.filter(publisher=user)
        return publications


class FeedList(ListAPIView):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs["username"])
        # 1
        # publications = Publication.objects.filter(publisher__in=user.profile.subscription.all())
        
        # 2
        publications = Publication.objects.filter(publisher__subscriber__in=[user.profile])
        
        # 3
        # publications = []
        # for publisher in user.profile.subscription.all():
        #     pubs = Publication.objects.filter(publisher=publisher)
        #     publications += pubs

        return publications


class ExploreView(ListAPIView):
    serializer_class = PublicationListSerializer

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs["username"])
        tags = HashTag.objects.filter(publication__publisher=user)
        publications = Publication.objects.filter(hashtag__in=tags).exclude(publisher=user)
        return publications


class LikeView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs["user_id"])
        publication = Publication.objects.get(id=self.kwargs["publication_id"])
        if Like.objects.filter(user=user, publication=publication).exists():
            Like.objects.get(user=user, publication=publication).delete()
            data = {"message": "like has been removed"}
        else:
            Like(user=user, publication=publication).save()
            data = {"user": user.id, "publication": publication.id}
        
        return Response(data)
