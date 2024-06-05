import random
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from testsapp.serializers import UserSerializer
from rest_framework import viewsets
from testsapp.serializers import *
from testsapp.models import *
from rest_framework.views import APIView

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
    # permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class TestListViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer


class RandomTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Test.objects.all()
        logical = request.query_params.get('logical', 'false').lower() == 'true'
        math = request.query_params.get('math', 'false').lower() == 'true'

        if logical and math:
            queryset = queryset.filter(test_type__test_type_name__in=['ლოგიკური', 'მათემატიკური'])
        elif logical:
            queryset = queryset.filter(test_type__test_type_name='ლოგიკური')
        elif math:
            queryset = queryset.filter(test_type__test_type_name='მათემატიკური')

        if queryset.exists():
            random_test = random.choice(queryset)
            serializer = TestListSerializer(random_test)
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No tests found matching the criteria.'})


