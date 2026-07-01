from django.db import models
from apps.courses.models import Course
from apps.teachers.models import Teacher


class Group(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        FINISHED = 'finished', 'Finished'
        PENDING = 'pending', 'Pending'

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='groups')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return self.name