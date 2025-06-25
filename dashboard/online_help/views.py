from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_your_activity, display_online_help_reference, display_online_help_user_guides, display_standalone_tools, display_pdf_documents, display_documentation

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ColorCommentForm, EditDocuForm

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
        'comments': 'ERD Something here'
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


def tasks_edit(request):
    ctx = {
        'radiant_documentation':display_documentation.section_data_radiant_docu,
    }
    return render(request, 'online_help/tasks_edit.html', context=ctx)


# Temporary in-memory storage (not persistent)
DOCUMENTATION_LIST = [
    "Online Help User Guides",
    "Online Help Reference",
    "Standalone Tools",
    "PDF Documents"
]

# Make sure to import EditDocuForm at the top of the file:
# from .forms import DocumentationForm

def documentation_edit(request):
    if request.method == 'POST':
        form = EditDocuForm(request.POST)
        if form.is_valid():
            doc_name = form.cleaned_data.get('documentation') or "Untitled"
            DOCUMENTATION_LIST.append(doc_name)
            documentation = form.cleaned_data['documentation']
            section = form.cleaned_data['section']
            subsection = form.cleaned_data['subsection']
            writer = form.cleaned_data['writer']
            color = form.cleaned_data['color']
            # return redirect('online_help/success.html')
            return render(request, 'online_help/success_documentation.html', 
                          {'form': form, 
                           'docs': DOCUMENTATION_LIST, 
                           'documentation': documentation,
                           'section': section,
                           'subsection': subsection,
                           'writer': writer,
                           'color': color,
                           })
    else:
        form = EditDocuForm()

    return render(request, 'online_help/documentation_edit.html', {
        'form': form,
        'docs': DOCUMENTATION_LIST
    })


# def documentation_edit(request):
#     if request.method == 'POST':
#         form = EditDocuForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('documentation_edit')
#     else:
#         form = EditDocuForm()

# #     docs = Documentation.objects.all()
#     return render(request, 'online_help/documentation_edit.html', {'form': form, 'docs': docs})


# def per_section(request, section_name):
#     ctx = {
#         'section_user_guide':display_online_help_user_guides.section_data_user_guide,
#         'section_reference': display_online_help_reference.section_data_reference,
#         'section_standalone': display_standalone_tools.section_data_standalone,
#         'section_pdf': display_pdf_documents.section_data_pdf,
#     }
#     return render(request, 'online_help/per_section.html', context=ctx)