from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos =  Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todos/index.html', context)


def detail(request, todo_pk):
    todo_pk = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo_pk,
    }
    
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title_1 = request.POST.get('title')
    content_1 = request.POST.get('content')
    completed_1 = request.POST.get('completed')
    priority_1 = request.POST.get('priority')
    deadline_1 = request.POST.get('deadline')
    
    todo = Todo(title=title_1, content=content_1, completed=completed_1, priority=priority_1, deadline=deadline_1)
    todo.save()
    
    return redirect('todos_app:detail', todo.pk)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos_app:index')


def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo,
    }
    
    return render(request, 'todos/edit.html', context)

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.completed = request.POST.get('completed')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')

    todo.save()
    
    return redirect('todos_app:detail', todo.pk)