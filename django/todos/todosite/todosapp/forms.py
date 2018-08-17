
from django import forms
from .models import Todo

class TodoForm(forms.Form):
	todo_text = forms.CharField(label="", max_length=250, widget=forms.TextInput(attrs={'class': 'main-input', 'placeholder': 'Enter your task...'}))

class TodoModelForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['todo_text']
		labels = {
			'todo_text': ""
		}
		widgets = {
			'todo_text': forms.TextInput(attrs={'class': 'main-input', 'placeholder': 'Enter your task...'})
		}