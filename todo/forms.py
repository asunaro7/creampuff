from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','category','deadline_date','level')
        widgets = {
            'deadline_date': forms.SelectDateWidget
        }
