from django.db import IntegrityError
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from chat.models import *
# Create your views here.

class Profile(ListView):
    model = User
    template_name = 'profile.html'
    
def Logout(request):
        logout(request)
        redirect('')
        
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
            
    if password1 == password2:
        try:
            user = User.objects.create_user(username=username, password=password1, photo='gallery/images/defaultphoto.jpg')
        except IntegrityError:
            msg = 'Такой пользователь уже существует'
            return render(request, 'registration/signup.html', {'msg' : msg})
        
    return render(request, 'registration/signup.html')