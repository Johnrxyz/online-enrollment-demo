from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addStudent, name='add_student'),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.editInfo, name='edit'),
    path('profile/', views.profile, name='profile'),
    path('other-profile/<slug:studentIdentifier>/', views.otherProfile, name='otherProfile'),
    path('student-list/', views.studentList, name='studentList'),
]