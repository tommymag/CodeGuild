from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Todo
from .forms import TodoForm, TodoModelForm

# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user).order_by('-created_date')
    else:
        todo_list = []
    context = {
        'todos': todo_list,
        'form_type': 'html_form',
    }
    return render(request, 'todosapp/index_template.html', context)

@login_required
def add_view(request):
    if request.method == 'POST':
        text = request.POST['todo_text']
        new_todo = Todo(todo_text=text, user=request.user)
        new_todo.save()
    return redirect('todos:index_path')

@login_required
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todos:index_path')

@login_required
def markdone(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index_path')

# # Index using Django Form
def index_with_django_form(request):
    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user).order_by('-created_date')
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                todo_text = form.cleaned_data['todo_text']
                todo = Todo(todo_text=todo_text, user=request.user)
                todo.save()
        form = TodoForm()
    else:
        todo_list = []
    context = {
        'todos': todo_list, 
        'form': form, 
        'form_type': 'django_form'
    }
    return render(request, 'todosapp/index_template.html', context)

# # Index using Django ModelForm
def index_with_model_form(request):
    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user).order_by('-created_date')    
        if request.method == 'POST':
            form = TodoModelForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user = request.user
                user.save()
        form = TodoModelForm()
    else:
        todo_list = []
    context = {
        'todos': todo_list, 
        'form': form, 
        'form_type': 'model_form'
    }
    return render(request, 'todosapp/index_template.html', context)