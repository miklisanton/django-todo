from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-details'),
    path('add-todo/', views.add_todo, name='add-todo'),
]