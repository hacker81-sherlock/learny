from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

from .models import User

def home(request):
    return render(request, 'core/home.html', {
        'auth': False
    })

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {
                'error': 1
            })
        user = User(username=username, password=make_password(password))
        user.save()
        return redirect('login') 
    
    return render(request, 'core/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return redirect('home')
            return render(request, 'core/login.html', {
                'error':True
            })
       
        return render(request, 'core/login.html', {
            'error': True
        })     
    
    return render(request, 'core/login.html')
