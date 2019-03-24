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


    