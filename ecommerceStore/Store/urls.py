from django.urls import path, include
from Store import views as views



# Create your views here

urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('register_business/', views.register_business, name='register_business'),
]


