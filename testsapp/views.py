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
from django.db.models import Q

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


class GetQuizApiAPIView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Test.objects.all()
        cat1 = request.query_params.get('cat1')
        cat2 = request.query_params.get('cat2')
        cat3 = request.query_params.get('cat3')
        if cat1 == '' or cat2 == '' or cat3 == '':
            if cat1 == '':
                queryset = Category1.objects.all()
                serializer = Category1Serializer(queryset, many=True)
                return Response(serializer.data)
            else:
                if cat2 == '':
                    # print('cat1=', cat1)
                    queryset = Category2.objects.filter(category1__name=cat1)
                    serializer = Category2Serializer(queryset, many=True)
                    return Response(serializer.data)
                else:
                    if cat3 == '':
                        queryset = Category3.objects.filter(category2__category1__name=cat1, category2__name=cat2)
                        serializer = Category1Serializer(queryset, many=True)
                        return Response(serializer.data)
        else:
            quizNumb = request.query_params.get('quizNumb')
            queryset = queryset.filter(test_origin__category2__category1__name=cat1,
                                       test_origin__category2__name=cat2, test_origin__name=cat3)
            # print(cat1, cat2, cat3, quizNumb)
            if quizNumb == '':
                resultJson = {}
                resultList = []
                resultJson['quizzCount'] = queryset.count() // 2
                resultJson['imageUrl'] = Category2.objects.get(name=cat2).testImage.url if \
                    Category2.objects.filter(name=cat2).exists() else None
                resultList.append(resultJson)
                serializer = QuizListSerializer(resultList, many=True)
                return Response(serializer.data)
            else:
                start_query = ((int(quizNumb)-1)*2)
                end_query = ((int(quizNumb)-1)*2+2)
                queryset = queryset[start_query:end_query]
                serializer = TestListSerializer(queryset, many=True)
                return Response(serializer.data)




class CatFilterAPIView(APIView):

    def get(self, request, *args, **kwargs):
        catFilter = request.query_params.get('catFilter')
        queryset = Test.objects.filter(Q(test_origin__category2__name__contains=catFilter) |
                                             Q(test_origin__category2__category1__name__contains=catFilter))

        listQuiz = []

        while queryset.count() > 0:
            cat3 = queryset[0].test_origin.name
            cat2 = queryset[0].test_origin.category2.name
            cat1 = queryset[0].test_origin.category2.category1.name
            querysetTemp = queryset.filter(test_origin__category2__category1__name=cat1,
                                       test_origin__category2__name=cat2, test_origin__name=cat3)
            dr = {}

            dr['cat1'] = cat1
            dr['cat2'] = cat2
            dr['cat3'] = cat3
            dr['totalQuiz'] = querysetTemp.count() // 2
            dr['imageUrl'] = Category2.objects.get(name=cat2).testImage.url if \
                Category2.objects.filter(name=cat2).exists() else None
            listQuiz.append(dr)

            queryset = queryset.exclude(
                test_origin__category2__category1__name=cat1,
                test_origin__category2__name=cat2,
                test_origin__name=cat3
            )
        # print(listQuiz)
        serializer = QuizCategorySerializer(listQuiz, many=True)
        return Response(serializer.data)



class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)