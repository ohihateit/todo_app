from django.urls import path

from todos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_status, name='update_status')
]

