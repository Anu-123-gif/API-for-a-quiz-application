from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from classroom import serializers
from classroom import models
from rest_framework import filters
from django.db import transaction

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        elif request.user.is_student:
            return redirect('students:quiz_list')
        else:
            return redirect('admin:index')
    return render(request, 'classroom/home.html')

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns authToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token. """

        return ObtainAuthToken().post(request)

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username")


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        #student.interests.add(*self.cleaned_data.get('interests'))
        return user


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        elif request.user.is_student:
            return redirect('students:quiz_list')
        else:
            return redirect('admin:index')
    return render(request, 'classroom/home.html')
