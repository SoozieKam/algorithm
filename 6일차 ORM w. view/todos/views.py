from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    
    return render(request, 'todos/index.html', context)


def detail(request, todo_pk):
    todo_1 = Todo.objects.get(pk=todo_pk)
    context = {
        'todo_pk': todo_1,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title_1 = request.GET.get('title')
    content_1 = request.GET.get('content')
    completed_1 = request.GET.get('completed')
    priority_1 = request.GET.get('priority')
    deadline_1 = request.GET.get('deadline')
    
    a = Todo(title=title_1, content=content_1, completed=completed_1, priority=priority_1, deadline=deadline_1)
    a.save()
    
    return render(request, 'todos/create.html')