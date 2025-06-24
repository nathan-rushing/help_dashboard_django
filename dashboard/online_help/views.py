from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_your_activity, display_online_help_reference, display_online_help_user_guides, display_standalone_tools, display_pdf_documents

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ColorCommentForm


@login_required
def home(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/home.html', context=ctx)


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
def your_activity(request):
    ctx = {
        'users': display_your_activity.writer_column,
    }
    return render(request, 'online_help/your_activity.html', context=ctx)

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

def per_user(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/per_user.html', context=ctx)

# def per_user_edit(request):
#     ctx = {
#         'section_user_guide':display_online_help_user_guides.section_data_user_guide,
#         'section_reference': display_online_help_reference.section_data_reference,
#         'section_standalone': display_standalone_tools.section_data_standalone,
#         'section_pdf': display_pdf_documents.section_data_pdf,
#     }
#     return render(request, 'online_help/per_user_edit.html', context=ctx)

def per_section(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/per_section.html', context=ctx)

def per_subsection(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/per_subsection.html', context=ctx)

def per_documentation(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/per_documentation.html', context=ctx)


def per_user_edit(request):
    initial_data = {
        'color': 'Yellow',
        'comments': 'ERD 475'
    }

    if request.method == 'POST':
        form = ColorCommentForm(request.POST)
        if form.is_valid():
            # Process form data here
            color = form.cleaned_data['color']
            comments = form.cleaned_data['comments']
            return render(request, 'online_help/success.html', {'color': color, 'comments': comments})
    else:
        form = ColorCommentForm(initial=initial_data)

    context = {
        'form': form,
        'section': 'Getting Started',
        'subsection': 'Introduction',
        'writer': 'Ave Manriquez'
    }
    return render(request, 'online_help/per_user_edit.html', context)


# def per_section(request, section_name):
#     ctx = {
#         'section_user_guide':display_online_help_user_guides.section_data_user_guide,
#         'section_reference': display_online_help_reference.section_data_reference,
#         'section_standalone': display_standalone_tools.section_data_standalone,
#         'section_pdf': display_pdf_documents.section_data_pdf,
#     }
#     return render(request, 'online_help/per_section.html', context=ctx)