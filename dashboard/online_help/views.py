from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_online_help_reference, display_online_help_user_guides, display_standalone_tools, display_pdf_documents
from online_help.management.utility import display_users

def home(request):
    return render(request, 'online_help/home.html')

def tasks(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    # ctx = {
    #     'sections': display_online_help_user_guides.section_column,
    #     'subsections': display_subsections.subsection_column,
    # }
    # print(ctx)
    return render(request, 'online_help/tasks.html', context=ctx)

def users(request):
    ctx = {
        'users': display_users.writer_column,
    }
    return render(request, 'online_help/users.html', context=ctx)

def something(request):
    return render(request, 'online_help/something.html')