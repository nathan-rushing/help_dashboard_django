from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_online_help_reference, display_online_help_user_guides, display_standalone_tools, display_pdf_documents
from online_help.management.utility import display_users

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request, 'online_help/home.html')


@login_required
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


@login_required
def users(request):
    ctx = {
        'users': display_users.writer_column,
    }
    return render(request, 'online_help/users.html', context=ctx)

@login_required
def erd(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/erd.html', context=ctx)


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('online_help:home')  # Redirect to dashboard or home
#         else:
#             messages.error(request, 'Invalid username or password.')

#     return render(request, 'online_help/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next') or 'online_help:home'
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')

    next_url = request.GET.get('next', '')
    return render(request, 'online_help/login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('online_help:login')
