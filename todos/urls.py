from django.urls import path

from todos import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('delete/<int:task_id>/', views.DeleteView.as_view(), name='delete_task'),
    path('update/<int:task_id>/', views.UpdateView.as_view(), name='update_status')
]

