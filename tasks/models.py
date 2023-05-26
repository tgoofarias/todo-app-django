from django.db import models
from users.models import Profile

import uuid

class TaskList(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='created_task_lists', null=True)
    contributors = models.ManyToManyField(Profile, related_name='contributed_task_lists')
    title = models.CharField(max_length=250, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)