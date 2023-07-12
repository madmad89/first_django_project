from django import forms
from django.forms import TextInput, EmailInput

from trainer.models import Trainer


# datetime-local pentru type atunci cand vreti sa aveti un calendar cu data si ora in formaular
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter course', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'department': TextInput(attrs={'placeholder': 'Please enter your department', 'class': 'form-control'}),
        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter course', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'department': TextInput(attrs={'placeholder': 'Please enter your department', 'class': 'form-control'}),
        }
