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
