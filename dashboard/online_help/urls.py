from django.urls import path
from . import views

app_name = 'online_help'
urlpatterns = [
    # path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home/writer/<int:pk>/', views.writer_detail, name='writer_detail'),

    
    path('', views.home_test, name='home_test'),
    path('home_test/', views.home_test, name='home_test'),
    path('home_test/per_user_test/<int:writer_pk>/', views.per_user_test, name='per_user_test'),
    path('home_test/per_user_test/<int:writer_pk>/per_user_edit_test/<int:task_pk>/', views.per_user_edit_test, name='per_user_edit_test'),
    path('home_test/per_user_test/<int:writer_pk>/per_subsection_test/<int:task_pk>/', views.per_subsection_test, name='per_subsection_test'),
    path('home_test/per_user_test/<int:writer_pk>/per_subsection_test/<int:task_pk>/per_user_edit_test/', views.per_subsection_edit_test, name='per_subsection_edit_test'),
    path('home_test/per_user_test/<int:writer_pk>/color/<str:color>/', views.tasks_by_color, name='tasks_by_color'),
    # path('home/per_user/<int:pk>/', views.per_user_test, name='per_user_test'),
    # path('home/per_subsection/<int:pk>/', views.per_subsection_test, name='per_subsection_test'),
    # path('home/per_user/<int:writer_pk>/per_subsection/<int:task_pk>/', views.per_subsection_test, name='per_user_test'),
    # path('erd/<int:pk>', views.erd, name='erd'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_test/', views.tasks_test, name='tasks_test'),
    path('tasks_test/tasks_edit_test/', views.tasks_edit_test, name='tasks_edit_test'),
    path('tasks_test/per_section_test/<int:section_pk>/', views.per_section_test2, name='per_section_test2'),
    path('tasks_test/per_subsection_task_test/<int:subsection_pk>/', views.per_subsection_task_test2, name='per_subsection_task_test2'),
    path('tasks_test/per_documentation_test/<int:document_pk>/', views.per_documentation_test, name='per_documentation_test'),
    path('tasks_test/per_documentation_test/<int:document_pk>/section_edit_test', views.section_edit_test, name='section_edit_test'),
    path('tasks_test/per_documentation_test/<int:document_pk>/per_section_test/<int:section_pk>/', views.per_section_test, name='per_section_test'),
    path('tasks_test/per_documentation_test/<int:document_pk>/per_section_test/<int:section_pk>/per_subsection_task_test/<int:subsection_pk>/', views.per_subsection_task_test, name='per_subsection_task_test'),
    path(
        'tasks_test/per_documentation_test/<int:document_pk>/section_edit_test/delete/<str:section_name>/',
        views.delete_section,
        name='delete_section'
    ),

    path(
        'tasks_test/per_documentation_test/<int:document_pk>/documentation_edit_test/',
        views.documentation_edit_test,
        name='documentation_edit_test'
    ),



    # path('per_documentation_test2/<str:document_name>/', views.per_documentation_test2, name='per_documentation_test2'),
    path('tasks_test/tasks_edit_test/per_documentation_test/<int:document_pk>/', views.per_documentation_test2, name='per_documentation_test2'),
    path('tasks_test/tasks_edit_test/documentation_edit_test/', views.documentation_edit_test, name='documentation_edit_test'),
    path(
        'tasks_test/documentation_edit_test/<int:document_pk>/delete/',
        views.delete_document,
        name='delete_document'
    ),


    path('tasks_test/per_section_test/<int:section_pk>/per_section_edit_test', views.per_section_edit_test, name='per_section_edit_test'),

    path(
        'tasks_test/per_section_test/<int:section_pk>/per_section_edit_test/delete/<int:task_pk>/',
        views.delete_subsection,
        name='delete_subsection'
    ),

    path('user_activity_test', views.user_activity_test, name='user_activity_test'),

    path('update-version/', views.update_version, name='update_version'),

    path('verify-password/', views.verify_password, name='verify_password'),



    # path('per_documentation_test/<int:pk>/', views.per_documentation_test2, name='per_documentation_test2'),



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
