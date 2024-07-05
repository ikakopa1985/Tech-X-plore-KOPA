from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from testsapp.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'answer_text', 'answers_image', 'is_correct']


class TestListSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, read_only=True, source='answers_set')

    class Meta:
        model = Test
        fields = [
            'id', 'test_origin', 'testText',
            'testDescription', 'testImage', 'answers'
        ]


class Category1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = ['id', 'name']


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = ['id', 'name']


class QuizCategorySerializer(serializers.Serializer):
    cat1 = serializers.CharField(max_length=255)
    cat2 = serializers.CharField(max_length=255)
    cat3 = serializers.CharField(max_length=255)
    totalQuiz = serializers.IntegerField()
    imageUrl = serializers.URLField()


class QuizListSerializer(serializers.Serializer):
    imageUrl = serializers.URLField()
    quizzCount = serializers.IntegerField()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'productImage']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserIdentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserIdent
        fields = ['full_name', 'birth_date', 'points', 'coins', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user_ident = UserIdent.objects.create(user=user, **validated_data)
            return user_ident
        else:
            raise serializers.ValidationError(user_serializer.errors)