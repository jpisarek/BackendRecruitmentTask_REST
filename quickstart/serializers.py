from rest_framework import serializers
from django.conf import settings
from django.db import models
from django.utils import timezone
from .models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('first_name', 'last_name', 'url')

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('first_name', 'last_name', 'url')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('value', 'task', 'candidate', 'recruiter', 'url')

class AllAboutSerializer(serializers.ModelSerializer):
    #author = CandidateSerializer(read_only=True)

    class Meta:
        model = AllAbout
        fields = ('candidate', 'url', 'grades')
        #read_only = ('grades', 'task')

#serializer = GradeSerializer(comment)
#serializer.data

    def create(self, validated_data):
        return AllAbout.objects.create(**validated_data)


    