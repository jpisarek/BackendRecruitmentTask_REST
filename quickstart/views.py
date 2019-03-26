from rest_framework import viewsets
from quickstart.serializers import *
from .models import Candidate, Recruiter, Task, Grade
from rest_framework.response import Response
import django

# API endpoint that allows groups to be viewed or edited.

class CandidateViewSet(viewsets.ModelViewSet):
   
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class RecruiterViewSet(viewsets.ModelViewSet):
    
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

class TaskViewSet(viewsets.ModelViewSet):
  
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GradeViewSet(viewsets.ModelViewSet):
   
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class AllAboutViewSet(viewsets.ModelViewSet):

    candidates = Candidate.objects.all()
    grades = Grade.objects.all()

    '''Poniższy fragment należy odkomentować po wykonaniu komendy: "python manage.py migrate" '''

    # for candidate in candidates:
    #     candidate.grades = Grade.objects.filter(candidate_id = candidate.id).values_list('value', flat=True)
    #     if len(candidate.grades) != 0:
    #         gradeSum = sum(candidate.grades)
    #         gradeLength = len(candidate.grades)
    #         candidate.avg = round(gradeSum/gradeLength, 2)
    #     else:    
    #         candidate.avg = 0
    #     print("Średnia ocen kandydata " + candidate.first_name + " " + candidate.last_name + ": " + str(candidate.avg))
    #     print("Oceny kandydata " + candidate.first_name + " " + candidate.last_name + ": " + str(candidate.grades))