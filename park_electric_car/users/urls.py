from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('check/', views.check, name='check'),
    path('profile/', views.login_redirect, name='login_redirect'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('cars/<int:pk>', views.car, name='car'),
    path('cars/new', views.CarInfoCreateView.as_view(), name='car_new'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
