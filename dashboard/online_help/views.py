from django.shortcuts import render
from django.http import HttpResponse
from online_help.management.utility import display_your_activity, display_online_help_reference, display_online_help_user_guides, display_standalone_tools, display_pdf_documents, display_documentation, db_online_help_user_guides

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import per_user_edit_Form, EditSectionForm, EditSubSectionForm, AddWriterForm
from .models import Writers, Task, TaskWriter, MajorDocu

# @login_required
# def home(request):
#     ctx = {
#         'db': db_online_help_user_guides,
#         'section_user_guide':display_online_help_user_guides.section_data_user_guide,
#         'section_reference': display_online_help_reference.section_data_reference,
#         'section_standalone': display_standalone_tools.section_data_standalone,
#         'section_pdf': display_pdf_documents.section_data_pdf,
#     }
#     return render(request, 'online_help/home.html', context=ctx)


# def home(request):
#     writers = Writers.objects.all()
#     return render(request, 'online_help/home.html', {'writers': writers})

# def home_test(request):
#     writers = Writers.objects.all()
#     task_writers = TaskWriter.objects.select_related('task', 'writer')
#     ctx = {
#         'task_writers': task_writers,
#         'writers': writers
#     }
#     return render(request, 'online_help/home_test.html', ctx)

from collections import defaultdict

def home_test(request):
    writers = Writers.objects.all()
    task_writers = TaskWriter.objects.select_related('task', 'writer')

    writer_tasks_grouped = {}

    for writer in writers:
        grouped_by_doc = defaultdict(list)
        for tw in task_writers:
            if tw.writer_id == writer.pk:
                grouped_by_doc[tw.task.document].append(tw)
        writer_tasks_grouped[writer.pk] = dict(grouped_by_doc)  # Convert to regular dict

    ctx = {
        'writers': writers,
        'writer_tasks_grouped': writer_tasks_grouped,
    }
    return render(request, 'online_help/home_test.html', ctx)

def home(request):
    writers = Writers.objects.all()
    return render(request, 'online_help/home.html', {'writers': writers})

def writer_detail(request, pk):
    writer = get_object_or_404(Writers, pk=pk)
    tasks = TaskWriter.objects.filter(writer=writer).select_related('task')
    return render(request, 'online_help/writer_detail.html', {'writer': writer, 'tasks': tasks})

# def per_user_test(request, writer_pk):
#     writer = get_object_or_404(Writers, pk=writer_pk)
#     tasks = TaskWriter.objects.filter(writer=writer).select_related('task')
#     return render(request, 'online_help/per_user_test.html', {'writer': writer, 'tasks': tasks})


def per_user_test(request, writer_pk):
    writer = get_object_or_404(Writers, pk=writer_pk)
    tasks = TaskWriter.objects.filter(writer=writer).select_related('task')

    grouped_tasks = defaultdict(list)
    for tw in tasks:
        grouped_tasks[tw.task.document].append(tw)

    return render(request, 'online_help/per_user_test.html', {
        'writer': writer,
        'grouped_tasks': dict(grouped_tasks),  # convert to regular dict
    })

def per_user_edit_test(request, writer_pk, task_pk):
    writer = get_object_or_404(Writers, pk=writer_pk)
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'POST':
        form = per_user_edit_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('online_help:per_user_edit_test', writer_pk=writer.pk, task_pk=task.pk)
    else:
        form = per_user_edit_Form(instance=task)

    return render(request, 'online_help/per_user_edit_test.html', {
        'form': form,
        'writer': writer,
        'task': task
    })


def per_subsection_test(request, writer_pk, task_pk):
    # Get the writer
    writer = get_object_or_404(Writers, pk=writer_pk)

    # Get the task
    task = get_object_or_404(Task, pk=task_pk)

    # Render the template
    return render(request, 'online_help/per_subsection_test.html', {
        'writer': writer,
        'task': task
    })


def per_subsection_edit_test(request, writer_pk, task_pk):
    writer = get_object_or_404(Writers, pk=writer_pk)
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'POST':
        form = per_user_edit_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('online_help:per_subsection_test', writer_pk=writer.pk, task_pk=task.pk)
    else:
        form = per_user_edit_Form(instance=task)

    return render(request, 'online_help/per_subsection_edit_test.html', {
        'form': form,
        'writer': writer,
        'task': task
    })


@login_required
def tasks(request):
    ctx = {
        'section_user_guide':display_online_help_user_guides.section_data_user_guide,
        'section_reference': display_online_help_reference.section_data_reference,
        'section_standalone': display_standalone_tools.section_data_standalone,
        'section_pdf': display_pdf_documents.section_data_pdf,
    }
    return render(request, 'online_help/tasks.html', context=ctx)


# def tasks_test(request):
#     task_writers = TaskWriter.objects.select_related('task', 'writer')
#     ctx = {
#         'task_writers': task_writers
#     }
#     return render(request, 'online_help/tasks_test.html', ctx)



def tasks_test(request):
    task_writers = TaskWriter.objects.select_related('task', 'writer')

    # Group by document
    grouped_by_document = defaultdict(list)
    for tw in task_writers:
        grouped_by_document[tw.task.document].append(tw)

    ctx = {
        'grouped_documents': dict(grouped_by_document),
    }
    return render(request, 'online_help/tasks_test.html', ctx)


# def per_documentation_test(request, task_pk):
#     # Get the writer
#     # writer = get_object_or_404(Writers, pk=writer_pk)

#     # Get the task
#     task = get_object_or_404(Task, pk=task_pk)

#     task_writers = TaskWriter.objects.select_related('task', 'writer')

#     # Group by document
#     grouped_by_document = defaultdict(list)
#     for tw in task_writers:
#         grouped_by_document[tw.task.document].append(tw)


#     # Render the template
#     return render(request, 'online_help/per_documentation_test.html', {
#         # 'writer': writer,
#         'task': task,
#         'task_writers': task_writers,
#         'grouped_documents': dict(grouped_by_document),
#     })

def per_documentation_test(request, document_pk):
    # Get one task to extract the document name
    reference_task = get_object_or_404(Task, pk=document_pk)
    document_name = reference_task.document

    # Get all tasks with the same document name
    tasks = Task.objects.filter(document=document_name)

    # Get one task per unique section
    seen_sections = set()
    unique_section_tasks = []
    for task in tasks:
        if task.section not in seen_sections:
            seen_sections.add(task.section)
            unique_section_tasks.append(task)

    return render(request, 'online_help/per_documentation_test.html', {
        'document_name': document_name,
        'document_pk': document_pk,
        'sections': unique_section_tasks,  # list of Task objects
    })



from django.shortcuts import render, get_object_or_404
from .models import Task

def per_section_test(request, document_pk, section_pk):
    reference_task = get_object_or_404(Task, pk=section_pk)
    document_name = reference_task.document
    section_name = reference_task.section

    tasks = Task.objects.filter(document=document_name, section=section_name)

    return render(request, 'online_help/per_section_test.html', {
        'document_name': document_name,
        'section_name': section_name,
        'tasks': tasks,
        'document_pk': document_pk,
        'section_pk': section_pk,
    })

def per_section_test2(request, section_pk):
    reference_task = get_object_or_404(Task, pk=section_pk)
    document_name = reference_task.document
    section_name = reference_task.section

    tasks = Task.objects.filter(document=document_name, section=section_name)

    return render(request, 'online_help/per_section_test.html', {
        'document_name': document_name,
        'section_name': section_name,
        'tasks': tasks,
        'document_pk': 1, # Replace with the actual document PK
        'section_pk': section_pk,
    })


from django.shortcuts import render, get_object_or_404
from .models import TaskWriter, Task

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, TaskWriter, Writers
from .forms import AddWriterForm
from django.contrib import messages

def per_subsection_task_test(request, document_pk, section_pk, subsection_pk):
    reference_task = get_object_or_404(Task, pk=subsection_pk)
    document_name = reference_task.document
    section_name = reference_task.section
    sub_section_name = reference_task.sub_section

    task_writers = TaskWriter.objects.select_related('writer', 'task').filter(
        task__document=document_name,
        task__section=section_name,
        task__sub_section=sub_section_name
    )

    form = AddWriterForm()

    # Handle form submission
    if request.method == 'POST':
        form = AddWriterForm(request.POST)
        if form.is_valid():
            writer_name = form.cleaned_data['writer'].strip()
            if writer_name:
                writer, created = Writers.objects.get_or_create(writer_name=writer_name)
                TaskWriter.objects.get_or_create(task=reference_task, writer=writer)
                messages.success(request, f"Writer '{writer_name}' added successfully.")
                return redirect(request.path_info)

    # Handle removal via GET parameter (?remove_writer=Name)
    writer_to_remove = request.GET.get('remove_writer')
    if writer_to_remove:
        try:
            writer = Writers.objects.get(writer_name=writer_to_remove)
            TaskWriter.objects.filter(task=reference_task, writer=writer).delete()
            messages.success(request, f"Writer '{writer_to_remove}' removed successfully.")
            return redirect(request.path_info)
        except Writers.DoesNotExist:
            messages.error(request, f"Writer '{writer_to_remove}' not found.")

    return render(request, 'online_help/per_subsection_task_test.html', {
        'document_name': document_name,
        'section_name': section_name,
        'sub_section_name': sub_section_name,
        'task_writers': task_writers,
        'form': form,
    })

def per_subsection_task_test2(request, subsection_pk):
    reference_task = get_object_or_404(Task, pk=subsection_pk)
    document_name = reference_task.document
    section_name = reference_task.section
    sub_section_name = reference_task.sub_section

    task_writers = TaskWriter.objects.select_related('writer', 'task').filter(
        task__document=document_name,
        task__section=section_name,
        task__sub_section=sub_section_name
    )

    form = AddWriterForm()

    # Handle form submission
    if request.method == 'POST':
        form = AddWriterForm(request.POST)
        if form.is_valid():
            writer_name = form.cleaned_data['writer'].strip()
            if writer_name:
                writer, created = Writers.objects.get_or_create(writer_name=writer_name)
                TaskWriter.objects.get_or_create(task=reference_task, writer=writer)
                messages.success(request, f"Writer '{writer_name}' added successfully.")
                return redirect(request.path_info)

    # Handle removal via GET parameter (?remove_writer=Name)
    writer_to_remove = request.GET.get('remove_writer')
    if writer_to_remove:
        try:
            writer = Writers.objects.get(writer_name=writer_to_remove)
            TaskWriter.objects.filter(task=reference_task, writer=writer).delete()
            messages.success(request, f"Writer '{writer_to_remove}' removed successfully.")
            return redirect(request.path_info)
        except Writers.DoesNotExist:
            messages.error(request, f"Writer '{writer_to_remove}' not found.")

    return render(request, 'online_help/per_subsection_task_test.html', {
        'document_name': document_name,
        'section_name': section_name,
        'sub_section_name': sub_section_name,
        'task_writers': task_writers,
        'form': form,
    })





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
        'comments': 'ERD-05.08 (DNG-22491) – Request for adding "percentage" view in Report Summary and Run Manager\n'
        '--05/09/2025: Documentation is done, Manish has reviewed and approved updates. Changes here: User Guides > Managing Projects > Viewing Logs and Reports\n\n'
        'ERD-05.10 (DNG-21175) – Enhancement Request - Breakdowns of Runtime for Different Compilation Stage\n'
        '--03/27/2025: In Progress. Per Manish, this is not yet implemented in Radiant.\n'
        '--05/05/2025: Done. Added to User Guides > Managing Projects > Viewing Logs and Reports section.\n\n'
        'ERD-10.02 (DNG-22646) – Report parameters on an entity with generics to show what has been passed\n'
        '--03/27/2025: In Progress. Verifying with Alka if this has been implemented in Radiant.\n'
        '--04/03/2025: Followed up with Alka.\n'
        '--04/07/2025: Added content to User Guides > Managing Projects > Viewing Logs and Reports and sent to Alka for review.\n'
    }

    if request.method == 'POST':
        form = per_user_edit_Form(request.POST)
        if form.is_valid():
            # Process form data here
            color = form.cleaned_data['color']
            comments = form.cleaned_data['comments']
            return render(request, 'online_help/success.html', {'color': color, 'comments': comments})
    else:
        form = per_user_edit_Form(initial=initial_data)

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
        form = per_user_edit_Form(request.POST)
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
        form = per_user_edit_Form()

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


def test(request):
    task_writers = TaskWriter.objects.select_related('task', 'writer')
    return render(request, 'online_help/test.html', {'task_writers': task_writers})


def test2(request):
    tasks = Task.objects.prefetch_related('taskwriter_set__writer')
    return render(request, 'online_help/test.html', {'tasks': tasks})


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