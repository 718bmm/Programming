from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def todo_view(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_view')
    else:
        form = TodoItemForm()
    todo_items = TodoItem.objects.all()
    return render(request, 'todoapp/todo_view.html', {'form': form, 'todo_items': todo_items})
