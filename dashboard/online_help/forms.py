from django import forms
from .models import Task, Writers, TaskWriter

COLOR_CHOICES = [
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Grey', 'Grey'),
    ('White', 'White'),
]

class per_user_edit_Form(forms.ModelForm):
    color = forms.ChoiceField(choices=COLOR_CHOICES, label='Color')
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}),
        label='Comments'
    )
    completion = forms.CharField(
        required=False,
        max_length=100,
        label='Completion',
        widget=forms.TextInput()
    )

    class Meta:
        model = Task
        fields = ['color', 'comments', 'completion']


# from django import forms
# from .models import Documentation

# class EditDocuForm(forms.ModelForm):
#     class Meta:
#         # model = Documentation
#         fields = ['documentation', 'section', 'subsection', 'writer', 'color']
#         widgets = {
#             'documentation': forms.TextInput(attrs={'placeholder': 'Documentation'}),
#             'section': forms.TextInput(attrs={'placeholder': 'Section'}),
#             'subsection': forms.TextInput(attrs={'placeholder': 'Subsection'}),
#             'writer': forms.TextInput(attrs={'placeholder': 'Writer'}),
#             'color': forms.TextInput(attrs={'placeholder': 'Color'}),
#         }


class EditDocuForm(forms.Form):
    document = forms.CharField(label='Document Name', required=False, max_length=255)
    # section = forms.CharField(required=False, max_length=255)
    # subsection = forms.CharField(required=False, max_length=255)
    # writer = forms.CharField(required=False, max_length=255)
    # color = forms.CharField(required=False, max_length=50)

# class EditSectionForm(forms.Form):
    # section = forms.CharField(required=False, max_length=255)
    # subsection = forms.CharField(required=False, max_length=255)
    # writer = forms.CharField(required=False, max_length=255)
    # color = forms.CharField(required=False, max_length=50)

class EditSectionForm(forms.ModelForm):
    writer = forms.ModelChoiceField(queryset=Writers.objects.all(), required=True)

    class Meta:
        model = Task
        fields = ['section', 'writer']


class EditSubSectionForm(forms.Form):
    subsection = forms.CharField(required=False, max_length=255)
    writer = forms.CharField(required=False, max_length=255)
    color = forms.CharField(required=False, max_length=50)

class AddWriterForm(forms.Form):
    writer = forms.ModelChoiceField(
        queryset=Writers.objects.all(),
        required=True,
        label='Select Writer',
        empty_label="Choose a writer",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

from django import forms
from .models import Writers, Task

from django import forms
from .models import Writers, Task

class AssignTaskForm(forms.Form):
    document = forms.ChoiceField(
        label="Document",
        required=True,
        widget=forms.Select(attrs={'id': 'id_document', 'class': 'form-control'})
    )
    section = forms.ChoiceField(
        label="Section",
        required=True,
        widget=forms.Select(attrs={'id': 'id_section', 'class': 'form-control'})
    )
    sub_section = forms.ChoiceField(
        label="Subsection",
        required=True,
        widget=forms.Select(attrs={'id': 'id_sub_section', 'class': 'form-control'})
    )
    writer = forms.ModelChoiceField(
        queryset=Writers.objects.all(),
        label="Writer",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate document dropdown with distinct document names
        documents = Task.objects.values_list('document', flat=True).distinct()
        self.fields['document'].choices = [('', 'Select document')] + [(doc, doc) for doc in documents]

        # Leave section and sub_section empty; they will be filled via JavaScript
        self.fields['section'].choices = [('', 'Select section')]
        self.fields['sub_section'].choices = [('', 'Select subsection')]
