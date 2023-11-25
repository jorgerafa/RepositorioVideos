from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError

# Create your views here.

def base(request):
    
    return render(request, "user/base.html")

# ----Autenticar usuario----
def sign_in(request):
    
    if request.method == "POST":
        user=authenticate(request, username=request.POST['username'],
                          password=request.POST['password'])
        if user is None:
            return render(request, "User/sign_in.html",
                          {
                           "form": AuthenticationForm,
                           "error": 'El usuario o la contraseña es incorrecta'
                           })
        else:
            login(request, user)
            return render('home')
    
    return render(request, "User/sign_in.html", {"form": AuthenticationForm})

# ----Registrar usuario----
def register(request):
    
    if request.method == "POST":
        if request.POST['username'] and request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],
                                              password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, "User/register.html",
                              {
                                  "form": UserCreationForm,
                                  "error": "The user already exists"
                                })
    return render(request, "User/register.html",{"form": UserCreationForm})
            
        
