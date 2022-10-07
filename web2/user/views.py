from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)

        if signupForm.is_valid():
            signupForm.save()
            return redirect('/user/login')
    else:
        signupForm = UserCreationForm()
    return render(request, 'user/signup.html', {'signupForm':signupForm})

def login(request):
    if request.method == 'POST':
        loginForm = AuthenticationForm(request, request.POST)

        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('/board/list/')
        else:
            return redirect('/user/login')
    else:
        loginForm = AuthenticationForm()

    return render(request, 'user/login.html', {'loginForm':loginForm})

def logout(request):
    auth_logout(request)
    return redirect('/user/login')