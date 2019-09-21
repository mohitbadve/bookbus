from django.urls import path,include
from app_version_1 import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('form-register/',views.registerForm),
    path('register/', views.register),
]