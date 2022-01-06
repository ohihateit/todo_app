from django.shortcuts import HttpResponse, render, redirect

from todos.forms import TaskForm
from todos.models import Task


def index(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")

    tasks = Task.objects.all()
    return render(request, "todos/index.html", {"task_form": form, "tasks": tasks})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

    return redirect("index")


def update_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()

    return redirect("index")
