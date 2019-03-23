from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Candidate(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Recruiter(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Task(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Grade(models.Model):
    value = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(2)])
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __int__(self):
        return self.value()


class AllAbout(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    #task = models.ForeignKey(Task, on_delete=models.CASCADE)
    grades = models.ManyToManyField(Grade)


    def __str__(self):
        return self.candidate()
        return self.grades()


   