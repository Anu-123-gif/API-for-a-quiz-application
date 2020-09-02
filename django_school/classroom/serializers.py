from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        """Create and return a new user."""

        user = models.User(
            username=validated_data["username"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
