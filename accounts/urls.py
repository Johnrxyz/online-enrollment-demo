from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ResetPasswordView
from . import views
urlpatterns = [
    path('student-register/', views.studentRegister,  name='studentRegister'),
    path('student-login/', views.studentLogin, name='studentLogin'),
    path('logout/', views.logoutView, name = 'logout'), 
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]