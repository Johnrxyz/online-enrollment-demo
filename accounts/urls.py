from django.urls import path
from . import views
urlpatterns = [
    path('student-register/', views.studentRegister,  name='studentRegister'),
    path('student-login/', views.studentLogin, name='studentLogin'),
    path('logout/', views.logoutView, name = 'logout'), 
]