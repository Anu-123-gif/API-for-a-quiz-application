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
