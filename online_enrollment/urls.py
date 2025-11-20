from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addStudent, name='add_student'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/', views.editInfo, name='edit'),
]