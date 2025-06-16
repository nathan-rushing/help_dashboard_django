from django.shortcuts import render
from django.http import HttpResponse
from dashboard.online_help.management.utility import display_online_help_user_guides
from online_help.management.utility import display_subsections, display_users

def home(request):
    return render(request, 'online_help/home.html')

def tasks(request):
    ctx = {
        'sections': display_online_help_user_guides.section_column,
        'subsections': display_subsections.subsection_column,
    }
    # print(ctx)
    return render(request, 'online_help/tasks.html', context=ctx)

def users(request):
    ctx = {
        'users': display_users.writer_column,
    }
    return render(request, 'online_help/users.html', context=ctx)

def something(request):
    return render(request, 'online_help/something.html')