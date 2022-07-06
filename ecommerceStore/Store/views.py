# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from Store.forms import *
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import login, logout, authenticate

# # Create your views here

def base(request):
    context = {}
    return render(request, 'base.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)


def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password1')
#         password2 = request.POST.get('password2')
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if password == password2:
#                 login(request, user)
#                 return redirect('home')
#             else :
#                 messages.error(request, "Passwords don't match.")
#         else:
#             messages.error(request, "User doesn't exist.")
    context = {}
    return render(request, 'login.html',context)

def registerPage(request):
#     form = createUser()
#     if request.method == 'POST':
#         form = createUser(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             messages.error(request, 'User already registered')
    context = {}
    return render(request, 'register_user.html',context) 




def register_business(request):
#     form = createBusiness()
#     if request.method == 'POST':
#         form = createBusiness(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             messages.error(request, 'Business already registered')
    context = {}
    return render(request, 'register_business.html',context)