from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_your_activity, display_online_help_reference, display_online_help_user_guides, display_standalone_tools, display_pdf_documents, display_documentation

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ColorCommentForm, EditDocuForm, EditSectionForm, EditSubSectionForm, AddWriterForm

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

# Temporary in-memory storage (not persistent)
SECTION_LIST = [
    "Getting Started with Radiant",
    "Managing Projects",
    "Securing the Design",
    "Simulating the Design",
    "Applying Design Constraints",
    "Implementing the Design",
    "Using Incremental Design Flow",
    "Analyzing Static Timing",
    "Analyzing Power Consumption",
    "Analyzing Signal Integrity",
    "Programming the FPGA",
    "Testing and Debugging On-Chip",
    "Applying Engineering Change Orders",
]

def section_edit(request):
    if request.method == 'POST':
        form = EditSectionForm(request.POST)
        if form.is_valid():
            # doc_name = form.cleaned_data.get('documentation') or "Untitled"
            # DOCUMENTATION_LIST.append(doc_name)
            # documentation = form.cleaned_data['documentation']
            section = form.cleaned_data['section']
            subsection = form.cleaned_data['subsection']
            writer = form.cleaned_data['writer']
            color = form.cleaned_data['color']
            # return redirect('online_help/success.html')
            return render(request, 'online_help/success_section.html', 
                          {'form': form, 
                           'docs': SECTION_LIST, 
                        #    'documentation': documentation,
                           'section': section,
                           'subsection': subsection,
                           'writer': writer,
                           'color': color,
                           })
    else:
        form = EditSectionForm()

    return render(request, 'online_help/section_edit.html', {
        'form': form,
        'docs': SECTION_LIST
    })

GETTING_STARTED_LIST = [
    "Introduction",
    "Tutorials",
    "User Guides",
    "Getting Help",
    "Debugging the Software License",
    "Copyright, Trademarks, and Disclaimers",
    "Introduction",
    "Running the Radiant Software",
    "Creating a New Project",
    "Modifying a Project",
    "Importing Lattice Diamond Projects",
    "Targeting a Device",
    "Viewing Project Properties",
    "Saving Project Files",
    "Managing Project Sources",
    "Working with Implementations",
    "Using Strategies",
    "Analyzing a Design",
    "Running Processes",
    "Clearing Tool Memory",
    "Setting Options for Synthesis and Simulation",
    "Finding Results",
    "Viewing Logs and Reports",
    "Setting Tool and Environment Options",
    "Introduction",
    "HDL Design Entry",
    "Block-Based Design - Using Macro Blocks",
    "Packaging IP Using Radiant IP Packager",
    "Designing with Soft IP, Modules, and PMI",
    "Introduction",
    "HDL File Encryption Steps",
    "Synthesizing Encrypted IP",
    "Cross-probing in Encrypted Design",
    "Secure Objects in the Design",
    "Securing the Bitstream",
    "Introduction",
    "Simulation in the Radiant Software",
    "Timing Simulation",
    "Third-Party Simulators",
    "Introduction",
    "Unified Constraint Flow",
    "Understanding Implications of Radiant Constraint Flows",
    "Applying Differential Signal Design Constraints",
    "Timing and Physical Constraints",
    "Checking Constraint Coverage",
    "Migrating from Former Lattice Diamond Preferences",
    "Migrating Pin Assignments",
    "Using Radiant Software Pre-Synthesis Constraints",
    "Constraint Propagation",
    "Using Radiant Tools",
    "Applying Radiant Software Physical Constraints",
    "Constraint Conflict Resolution",
    "Checking Design Rules",
    "Analyzing SSO",
    "Exporting Pin Files",
    "Introduction",
    "Synthesizing the Design",
    "Mapping",
    "Place and Route",
    "Bit Generation",
    "nan",
    "SEI Editor",
    "Running the Incremental Design Flow",
    "Introduction",
    "Options for Timing Analysis Reports",
    "Running Post-Synthesis Constraint Scenario Timing Reports",
    "Reading Timing Analysis Reports",
    "Using Timing Analyzer",
    "Using StandAlone Timing Analyzer",
    "Introduction",
    "Starting Power Calculator from Radiant",
    "Starting Power Calculator as a Stand-Alone Tool",
    "Running Power Calculator from the Tcl Console",
    "Power Analysis Design Flow",
    "Inputs",
    "Outputs",
    "Static and Dynamic Power Consumption",
    "Activity Factor Calculation",
    "Enable Factor Calculation",
    "Power Calculator Window Features",
    "Working with Power Calculator Files",
    "Entering Data",
    "Calculator Sleep Mode",
    "Reverting to Calculation Mode",
    "Changing the Global Default Activity Factor",
    "Importing a Value Change Dump (.vcd) File",
    "Changing the Global Default Frequency Setting",
    "Estimating Resource Usage",
    "Estimating Routing Resource Usage",
    "Running Immediate Calculation",
    "Controlling Operating Temperature",
    "Controlling Power Options for Low-Power Devices",
    "Comparing Power Consumption Among Multiple Implementations",
    "Viewing and Printing Results",
    "Device Support",
    "Introduction",
    "Introduction",
    "About the Programmer Window",
    "File Formats",
    "SPI Flash Support",
    "Using the Radiant Programmer",
    "Programmer Options",
    "Programming and Configuring iCE40 Devices with Programmer",
    "Programming and Configuring LAV-AT, LFCPNX, LFD2NX, LFMNX, LFMXO5, LIFCL, MachXO3D, MachXO3L, MachXO3LF, UT24C or UT24CP Devices with Programmer",
    "Deploying the Design with Deployment Tool",
    "Debugging SVF, STAPL, and VME Files",
    "Download Debugger Options",
    "Using Programming File Utility",
    "Programming File Utility Options",
    "Introduction",
    "About Reveal Logic Analysis",
    "Creating Reveal Modules",
    "Performing Logic Analysis",
    "Eye-Opening Monitor",
    "Reveal Controller",
    "Introduction",
    "Editing sysIO Settings in ECO Editor",
    "Setting Memory Initialization Values in ECO Editor",
    "Running Design Rule Check",
]

def per_section_edit(request):
    if request.method == 'POST':
        form = EditSubSectionForm(request.POST)
        if form.is_valid():
            # doc_name = form.cleaned_data.get('documentation') or "Untitled"
            # DOCUMENTATION_LIST.append(doc_name)
            # documentation = form.cleaned_data['documentation']
            subsection = form.cleaned_data['subsection']
            writer = form.cleaned_data['writer']
            color = form.cleaned_data['color']
            # return redirect('online_help/success.html')
            return render(request, 'online_help/success_per_section_edit.html', 
                          {'form': form, 
                           'docs': GETTING_STARTED_LIST, 
                        #    'documentation': documentation,
                        #    'section': section,
                           'subsection': subsection,
                           'writer': writer,
                           'color': color,
                           })
    else:
        form = EditSubSectionForm()

    return render(request, 'online_help/per_section_edit.html', {
        'form': form,
        'docs': GETTING_STARTED_LIST
    })


def per_subsection_task(request):
    if request.method == 'POST':
        form = AddWriterForm(request.POST)
        if form.is_valid():
            # doc_name = form.cleaned_data.get('documentation') or "Untitled"
            # DOCUMENTATION_LIST.append(doc_name)
            # documentation = form.cleaned_data['documentation']
            # section = form.cleaned_data['section']
            # subsection = form.cleaned_data['subsection']
            writer = form.cleaned_data['writer']
            # return redirect('online_help/success.html')

            return render(request, 'online_help/success_per_subsection_task.html', 
                          {'form': form, 
                           'docs': SECTION_LIST, 
                        #    'documentation': documentation,
                           'writer': writer,
                           })
    else:
        form = AddWriterForm()

    return render(request, 'online_help/per_subsection_task.html', {
        'form': form,
        'docs': SECTION_LIST
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