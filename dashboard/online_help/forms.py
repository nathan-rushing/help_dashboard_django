from django import forms
from .models import Task


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


from django import forms
from .models import Task, Writers

class EditSectionForm(forms.ModelForm):
    writer = forms.ModelChoiceField(queryset=Writers.objects.all(), required=True)

    class Meta:
        model = Task
        fields = ['sub_section', 'writer']


class EditSubSectionForm(forms.Form):
    subsection = forms.CharField(required=False, max_length=255)
    writer = forms.CharField(required=False, max_length=255)
    color = forms.CharField(required=False, max_length=50)

class AddWriterForm(forms.Form):
    # section = forms.CharField(required=False, max_length=100, label='Section', widget=forms.TextInput)
    # subsection = forms.CharField(required=False, max_length=100, label='Subsection', widget=forms.TextInput)
    writer = forms.CharField(required=False, max_length=100, label='Name', widget=forms.TextInput)
