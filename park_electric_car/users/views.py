from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView

from .forms import UserRegisterForm
from .models import CarInfo, User, UserInfo


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def login(request):
    template = 'users/login.html'
    return render(request, template)


def profile(request, pk):
    user = User.objects.get(pk=pk)
    user_infos = UserInfo.objects.filter(user=user)
    cars = []
    for user_info in user_infos:
        cars += CarInfo.objects.filter(userinfo=user_info)
    if cars:
        context = {
            'user': user,
            'user_info': user_info,
            'cars': cars,
        }
    else:
        context = {
            'user': '',
            'user_info': '',
            'cars': '',
        }
    template = 'users/profile.html'
    return render(request, template, context)


def car(request, pk1, pk2):
    user = User.objects.get(pk=pk1)
    user_infos = UserInfo.objects.filter(user=user)
    car = CarInfo.objects.get(pk=pk2)
    print(car)
    if car:
        context = {
            'car': car,
        }
    else:
        context = {
            'car': '',
        }
    template = 'users/car.html'
    print(context)
    return render(request, template, context)


def login_redirect(request):
    pk = request
    print(type(pk))
    return reverse('profile', args=(pk,))
