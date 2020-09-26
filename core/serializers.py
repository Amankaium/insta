from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    subscription_count = serializers.SerializerMethodField()
    subscriber_count = serializers.SerializerMethodField()
    publication_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "user", "subscription_count",
            "subscriber_count", "publication_count"
        ]
    
    def get_subscription_count(self, obj):
        return obj.subscription.all().count()
    
    def get_subscriber_count(self, obj):
        return obj.user.subscriber.all().count()

    def get_publication_count(self, obj):
        return obj.user.publication.filter(deleted=False).count()


class UserSerializer(serializers.ModelSerializer):
    subscription_count = serializers.SerializerMethodField()
    subscriber_count = serializers.SerializerMethodField()
    publication_count = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "subscription_count",
            "subscriber_count",
            "publication_count",
            "description",
            "photo",
        ]

    def get_subscription_count(self, obj):
        return obj.profile.subscription.all().count()
    
    def get_subscriber_count(self, obj):
        return obj.subscriber.all().count()

    def get_publication_count(self, obj):
        return obj.publication.filter(deleted=False).count()
    
    def get_description(self, obj):
        return obj.profile.description

    def get_photo(self, obj):
        return obj.profile.photo.url


class UserListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "photo"]

    def get_photo(self, obj):
        return obj.profile.photo.url


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class ProfileEditSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    user = UserEditSerializer()

    class Meta:
        model = Profile
        fields = ["user", "description", "photo"]
    
    # def update(self, instance, validated_data):
    #     nested_serializer = self.fields['user']
    #     nested_instance = instance.user
    #     # note the data is `pop`ed
    #     nested_data = validated_data.pop('user')
    #     nested_serializer.update(nested_instance, nested_data)
    #     # this will not throw an exception,
    #     # as `profile` is not part of `validated_data`
    #     return super(ProfileEditSerializer, self).update(instance, validated_data)


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["description", "photo"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
