from rest_framework import serializers
from classroom.models import (Answer, Question, Student, StudentAnswer,
                              Subject, User)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        """Create and return a new user."""

        user = User(
            username=validated_data["username"],
        )

        user.is_student = True
        user.set_password(validated_data["password"])
        user.save()
        student = Student.objects.create(user=user)

        return user
