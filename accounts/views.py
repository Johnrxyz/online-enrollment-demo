from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def studentRegister(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account made successful')
            return redirect('studentLogin')
        else:
            messages.error(request, f'Form is invalid')
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def studentLogin(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username= username, password = password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')

                return redirect('profile')
            else:
                messages.error(request, 'No user found')
        else:
            print(form.errors)
            messages.error(request, 'Invalid username or password')
    form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logoutView(request):
    messages.success(request, f'Log out successful {request.user}!')
    logout(request)

    return redirect('studentLogin')



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password_reset_done')