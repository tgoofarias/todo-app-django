from django.forms import ModelForm
from .models import TaskList, Task


class TaskListForm(ModelForm):
    class Meta:
        model = TaskList
        exclude = ['creator', 'contributors']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['task_list', 'is_complete']