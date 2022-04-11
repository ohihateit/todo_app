from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import HttpResponse, render, redirect
from django.views import View

from todos.forms import TaskForm
from todos.models import Task


class IndexView(View):
    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, "todos/index.html", {"task_form": form, "tasks": tasks})


    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")


class DeleteView(View):
    def get(request: WSGIRequest, task_id: int) -> HttpResponse:  # Maybe post?
        task = Task.objects.get(pk=task_id)
        task.delete()

        return redirect("index")


class UpdateView(View):
    def GET(request: WSGIRequest, task_id: int) -> HttpResponse:  # Maybe post?
        task = Task.objects.get(pk=task_id)
        task.completed = True
        task.save()

        return redirect("index")
