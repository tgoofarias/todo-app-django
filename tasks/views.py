from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Task
from .forms import TaskListForm, TaskForm


@login_required(login_url='login')
def task_lists(request):
    profile = request.user.profile
    task_lists = profile.contributed_task_lists.all()
    context = {
        'task_lists': task_lists
    }
    return render(request, 'tasks/task_lists.html', context)


@login_required(login_url='login')
def create_task_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            profile = request.user.profile
            task_list.creator = profile
            task_list.save() # Salva a TaskList para obter um ID válido
            task_list.contributors.add(profile)

            return redirect('task_lists')

    form = TaskListForm()
    context = {
        'form': form
    }
    return render(request, 'tasks/task_list_form.html', context)


@login_required(login_url='login')
def update_task_list(request, pk):
    profile = request.user.profile
    task_list = profile.contributed_task_lists.get(id=pk)

    if request.method == 'POST':
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
            return redirect('task_lists')

    form = TaskListForm(instance=task_list)
    context = {
        'form': form
    }
    return render(request, 'tasks/task_list_form.html', context)


@login_required(login_url='login')
def delete_task_list(request, pk):
    profile = request.user.profile
    task_list = profile.created_task_lists.get(id=pk)

    if request.method == 'POST':
        task_list.delete()
        return redirect('task_lists')
    
    context = {
        'object': task_list
    }
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def task_list(request, pk):
    profile = request.user.profile
    task_list = profile.contributed_task_lists.get(id=pk)
    tasks = task_list.task_set.all()
    context = {
        'task_list': task_list,
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context)


@login_required(login_url='login')
def add_contributor(request, pk):
    if request.method == 'POST':
        profile = request.user.profile
        task_list = profile.created_task_lists.get(id=pk)
        username = request.POST['username'].lower()
        profile = User.objects.get(username=username).profile
        task_list.contributors.add(profile)
        return redirect('task_list', pk)


@login_required(login_url='login')
def create_task(request, pk):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            profile = request.user.profile
            task_list = profile.contributed_task_lists.get(id=pk)
            task.task_list = task_list
            task.save()
            return redirect('task_list', pk)

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'tasks/task_form.html', context)


@login_required(login_url='login')
def update_task(request, pk):
    task_list = Task.objects.get(id=pk).task_list
    profile = request.user.profile

    if profile not in task_list.contributors.all():
        return

    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task_list_id = task.task_list.id 
            task.save()
            return redirect('task_list', task_list_id)

    form = TaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'tasks/task_form.html', context)


@login_required(login_url='login')
def delete_task(request, pk):
    task_list = Task.objects.get(id=pk).task_list
    profile = request.user.profile

    if profile not in task_list.contributors.all():
        return

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task_list_id = task.task_list.id
        task.delete()
        return redirect('task_list', task_list_id)
    
    context = {
        'object': task
    }
    return render(request, 'delete_template.html', context)