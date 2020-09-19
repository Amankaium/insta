from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from .models import Publication
from .serializers import PublicationSerializer


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
    return Response(serializer.data)