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

class AllAboutViewSet(viewsets.ModelViewSet):

    candidates = Candidate.objects.all()
    grades = Grade.objects.all()

    for candidate in candidates:
        candidate.grades = Grade.objects.filter(candidate_id = candidate.id).values_list('value', flat=True)
        print(str(len(candidate.grades)))
        print(str(candidate.grades))

        if len(candidate.grades) != 0:
            gradeSum = sum(candidate.grades)
            gradeLength = len(candidate.grades)
            candidate.avg = round(gradeSum/gradeLength, 2)
        else:    
            candidate.avg = 0
        print(str(candidate.avg))
        print("oceny " + candidate.last_name + " " + str(candidate.grades))