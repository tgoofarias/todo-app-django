from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('task_lists')

    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('User logged successfully')
            return redirect('task_lists')
        else:
            print('User is not authenticated')
    return render(request, 'users/login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('task_lists')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('task_lists')

    form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)