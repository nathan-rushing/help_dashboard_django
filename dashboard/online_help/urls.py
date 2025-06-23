from django.urls import path
from . import views

app_name = 'online_help'
urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('activity/', views.your_activity, name='activity'),
    path('erd/', views.erd, name='erd'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('per_subsection/', views.per_subsection, name='per_subsection'),
    # path('per_subsection/<str:section_name>/', views.per_subsection, name='per_subsection'),
]
