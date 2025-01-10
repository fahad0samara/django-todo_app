from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('completed/', views.completed,name='completed'), 
    path('remaining/', views.remaining,name='remaining'),
    path('add/', views.add_task,name='add_task'),
    path('delete/<int:task_id>/', views.delete_task,name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task,name='toggle_task'),
    path('task/<int:task_id>/', views.task_detail,name='task_detail'),
    path('task/<int:task_id>/comment/', views.add_comment, name='add_comment'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('categories/', views.manage_categories,name='manage_categories'),
    path('labels/', views.manage_labels, name='manage_labels'),
    path('labels/delete/<int:label_id>/', views.delete_label, name='delete_label'),
    path('labels/edit/<int:label_id>/', views.edit_label, name='edit_label'),
    path('calendar/', views.calendar_view, name='calendar'),
]