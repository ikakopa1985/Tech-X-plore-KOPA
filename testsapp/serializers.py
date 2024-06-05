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
            'id', 'test_origin', 'number', 'test_type', 'testText',
            'testDescription', 'testImage', 'answers'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserIdentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserIdent
        fields = ['full_name', 'personal_number', 'birth_date', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user_ident = UserIdent.objects.create(user=user, **validated_data)
            return user_ident
        else:
            raise serializers.ValidationError(user_serializer.errors)