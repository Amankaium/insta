from rest_framework.serializers import ModelSerializer
from .models import Publication

class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = ["pk", "image", "description", "publisher", "created"]