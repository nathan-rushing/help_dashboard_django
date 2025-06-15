from django.urls import path
from . import views

app_name = 'online_help'
urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('users/', views.users, name='users'),
    path('something/', views.something, name='something'),
]
