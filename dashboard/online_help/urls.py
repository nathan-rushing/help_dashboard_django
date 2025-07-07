from django.urls import path
from . import views

app_name = 'online_help'
urlpatterns = [
    # path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    # path('home/writer/<int:pk>/', views.writer_detail, name='writer_detail'),
    path('home_test/', views.home_test, name='home_test'),
    path('home_test/per_user_test/<int:writer_pk>/', views.per_user_test, name='per_user_test'),
    path('home_test/per_user_test/<int:writer_pk>/per_subsection/<int:task_pk>/', views.per_subsection_test, name='per_subsection_test'),
    path('home_test/per_user_test/<int:writer_pk>/per_subsection/<int:task_pk>/per_user_edit_test/', views.per_subsection_edit_test, name='per_subsection_edit_test'),
    # path('home/per_user/<int:pk>/', views.per_user_test, name='per_user_test'),
    # path('home/per_subsection/<int:pk>/', views.per_subsection_test, name='per_subsection_test'),
    # path('home/per_user/<int:writer_pk>/per_subsection/<int:task_pk>/', views.per_subsection_test, name='per_user_test'),
    # path('erd/<int:pk>', views.erd, name='erd'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_test/', views.tasks_test, name='tasks_test'),
    path('tasks_test/per_documentation_test/<int:document_pk>/', views.per_documentation_test, name='per_documentation_test'),
    path('tasks_test/per_documentation_test/<int:document_pk>/per_section_test/<int:section_pk>/', views.per_section_test, name='per_section_test'),
    path('tasks_test/per_documentation_test/<int:document_pk>/per_section_test/<int:section_pk>/per_subsection_task_test/<int:subsection_pk>/', views.per_subsection_task_test, name='per_subsection_task_test'),

    path('activity/', views.your_activity, name='activity'),
    path('erd/', views.erd, name='erd'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('per_user/', views.per_user, name='per_user'),
    path('per_user_edit/', views.per_user_edit, name='per_user_edit'),
    path('per_section/', views.per_section, name='per_section'),
    path('per_subsection/', views.per_subsection, name='per_subsection'),
    path('per_subsection_task/', views.per_subsection_task, name='per_subsection_task'),
    path('per_documentation/', views.per_documentation, name='per_documentation'),
    path('tasks_edit/', views.tasks_edit, name='tasks_edit'),
    path('documentation_edit/', views.documentation_edit, name='documentation_edit'),
    path('section_edit/', views.section_edit, name='section_edit'),
    path('per_section_edit/', views.per_section_edit, name='per_section_edit'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    # path('color-comment/', views.color_comment_view, name='color_comment'),

    # path('per_subsection/<str:section_name>/', views.per_subsection, name='per_subsection'),
]
