from django.urls import path
from . import views

urlpatterns = [
    path('task-lists/', views.task_lists, name='task_lists'),
    path('create-task-list/', views.create_task_list, name='create_task_list'),
    path('update-task-list/<str:pk>/', views.update_task_list, name='update_task_list'),
    path('delete-task-list/<str:pk>/', views.delete_task_list, name='delete_task_list'),
    path('task-list/<str:pk>/', views.task_list, name='task_list'),
    path('task-list/<str:pk>/add-contributor/', views.add_contributor, name='add_contributor'),

    path('task-list/<str:pk>/create-task/', views.create_task, name='create_task'),
    path('update-task/<str:pk>/', views.update_task, name='update_task'),
    path('delete-task/<str:pk>/', views.delete_task, name='delete_task'),
]