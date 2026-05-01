from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('register/', views.RegisterView , name="register"),
    path('login/', views.LoginView , name="login"),
    path('logout/', views.LogOutView , name="logout"),
]


#           python manage.py runserver