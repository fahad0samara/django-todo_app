from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
     path('completed/', views.completed,name='completed'), 
        path('add_task/', views.add_task,name='add_task'),
        path('delete_task/', views.delete_task,name='delete'),
        path('remaining/', views.remaining,name='remaining'),
        path('task_detail/', views.task_detail,name='task_detail'),
]