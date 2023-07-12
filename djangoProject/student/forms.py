from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


# datetime-local pentru type atunci cand vreti sa aveti un calendar cu data si ora in formaular
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'age', 'email', 'description',
        #           'active', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(
                attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'})

        }

    def clean(self):
        cleaned_data = self.cleaned_data
        check_emails = Student.objects.filter(email=cleaned_data['email'])
        if check_emails:
            msg = 'Aceasta adresa de mail exista deja in db'
            self._errors['email'] = self.error_class([msg])

        get_start_date = cleaned_data['start_date']
        get_end_date = cleaned_data['end_date']
        if get_start_date > get_end_date:
            msg = 'Start date este mai mare decat end date'
            self.errors['start_date'] = self.error_class([msg])
        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'age', 'email', 'description',
        #           'active', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(
                attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'})

        }
