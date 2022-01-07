from django import forms
from django.forms import ModelForm

from todos.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the task here',
                'class': 'form-control'
            })
        }
