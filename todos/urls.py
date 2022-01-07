from django.views.generic import TemplateView
from django.urls import path

from todos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('not_found/', TemplateView.as_view(template_name="todos/not_found.html"), name="not_found"),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_status, name='update_status')
]

