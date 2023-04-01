from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.

TASK_URGENCY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    ]

# card model
class Card(models.Model):
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    taskid = models.UUIDField(primary_key=True, default=uuid.uuid1) 
    task_name = models.CharField(max_length=25, null=False, blank=False)
    task_progress = models.IntegerField(default=0)
    task_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    task_deadline_date = models.DateField(auto_now=False, default=datetime.date(2020,1,1))
    task_deadline_time = models.TimeField(auto_now=False, default=datetime.time(11, 59, 59))
    task_deadline = models.DateTimeField(auto_now=False, null=True)
    task_urgency = models.CharField(max_length=6,choices=TASK_URGENCY_CHOICES, default='low')
    task_status = models.BooleanField(default=False)

    def __str__(self):
        return (f'task {self.task_name} by {self.task_owner}')
    

# subcard model
class SubCard(models.Model):
    subtask_name = models.CharField(max_length=25, null=False, blank=False)
    subtask_time = models.DateTimeField(auto_now=True)
    task_name = models.ForeignKey(Card , on_delete=models.CASCADE)
    subtask_state = models.BooleanField(default=False)

    class Meta:
        unique_together = ('subtask_name', 'task_name',)

    def str(self):
        return (f'subtask {self.subtask_name} in task {self.task_name.task_name} by {self.task_name.task_owner}')