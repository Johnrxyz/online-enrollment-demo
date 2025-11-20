from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account made successful')
            return redirect('login')
        else:
            messages.error(request, 'Form is invalid')
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username= username, password = password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')

                return redirect('dashboard')
            else:
                messages.error(request, 'No user found')
        else:
            print(form.errors)
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logoutView(request):
    logout(request)

    return redirect('login')