from django import forms

COLOR_CHOICES = [
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Grey', 'Grey'),
    ('White', 'White'),
]

class ColorCommentForm(forms.Form):
    color = forms.ChoiceField(choices=COLOR_CHOICES, label='Color')
    comments = forms.CharField(widget=forms.Textarea, label='Comments')
    completion = forms.CharField(required=False, max_length=100, label='Completion', widget=forms.TextInput)

from django import forms
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
    documentation = forms.CharField(required=False, max_length=255)
    section = forms.CharField(required=False, max_length=255)
    subsection = forms.CharField(required=False, max_length=255)
    writer = forms.CharField(required=False, max_length=255)
    color = forms.CharField(required=False, max_length=50)

class EditSectionForm(forms.Form):
    section = forms.CharField(required=False, max_length=255)
    subsection = forms.CharField(required=False, max_length=255)
    writer = forms.CharField(required=False, max_length=255)
    color = forms.CharField(required=False, max_length=50)

class EditSubSectionForm(forms.Form):
    subsection = forms.CharField(required=False, max_length=255)
    writer = forms.CharField(required=False, max_length=255)
    color = forms.CharField(required=False, max_length=50)
