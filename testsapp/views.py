from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from testsapp.serializers import UserSerializer
from rest_framework import viewsets
from testsapp.serializers import *
from testsapp.models import *

# Create your views here.


def index(request):
    return render(request, template_name='testsapp/index.html')


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })


class UserIdentViewSet(viewsets.ModelViewSet):
    queryset = UserIdent.objects.all()
    serializer_class = UserIdentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestListViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer

