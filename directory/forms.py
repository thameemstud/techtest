from django.forms import ModelForm
from .models import Teacher,Subject
from django.forms import ModelMultipleChoiceField,CheckboxSelectMultiple,ValidationError



    

# Create the form class.
class TeacherForm(ModelForm):
    subject = ModelMultipleChoiceField(widget=CheckboxSelectMultiple(), queryset=Subject.objects.all())
    class Meta:
        model = Teacher
        fields = ['firstName', 'lastName', 'profilePicture', 'email', 'phone', 'roomNumber']

    def clean_subject(self):
        b = self.cleaned_data['subject']
        if b.count() > 5:
            raise ValidationError("Cannot assign more than 5 subject to a teacher.")
        return self.cleaned_data['subject']