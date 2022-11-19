from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('registration/', views.registration, name='registration'),
]