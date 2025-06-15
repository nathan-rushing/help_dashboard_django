from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_sections, display_subsections

def home(request):
    return render(request, 'online_help/home.html')

def tasks(request):
    ctx = {
        'sections': display_sections.section_column,
        'subsections': display_subsections.subsection_column,
    }
    print(ctx)
    return render(request, 'online_help/tasks.html', context=ctx)

def users(request):
    
    return render(request, 'online_help/users.html')

def something(request):
    return render(request, 'online_help/something.html')