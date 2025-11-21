from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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