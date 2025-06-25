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
    path('per_user/', views.per_user, name='per_user'),
    path('per_user_edit/', views.per_user_edit, name='per_user_edit'),
    path('per_section/', views.per_section, name='per_section'),
    path('per_subsection/', views.per_subsection, name='per_subsection'),
    path('per_documentation/', views.per_documentation, name='per_documentation'),
    path('tasks_edit/', views.tasks_edit, name='tasks_edit'),
    path('documentation_edit/', views.documentation_edit, name='documentation_edit'),
    path('section_edit/', views.section_edit, name='section_edit'),
    # path('color-comment/', views.color_comment_view, name='color_comment'),

    # path('per_subsection/<str:section_name>/', views.per_subsection, name='per_subsection'),
]
