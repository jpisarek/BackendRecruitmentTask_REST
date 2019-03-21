from rest_framework import viewsets
from quickstart.serializers import *
from .models import Candidate, Recruiter, Task, Grade

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
    