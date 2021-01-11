from django import forms
from .models import Teacher,Subject
# from django.forms import ModelMultipleChoiceField,CheckboxSelectMultiple,ValidationError
from django.core.validators import FileExtensionValidator


class FilterForm(forms.Form):
    filter_lastname = forms.CharField(required=False)
    filter_subject = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'textinput textInput form-control'

class BulkUploadForm(forms.Form):

    csv_file = forms.FileField(
                validators=[FileExtensionValidator(allowed_extensions=['csv'])]
            )
    zip_file = forms.FileField(
                validators=[FileExtensionValidator(allowed_extensions=['zip'])]
            )


