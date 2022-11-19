from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
# from ..expertises.models import CarInfo


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


# def profile(request, pk):
#     cars = CarInfo.objects.get(pk=pk)
#     context = {
#         'cars': cars,
#     }
#     template = 'users/profile.html'
#     return render(request, template, context)

# def registration(request):
#     template = 'users/registration.html'
#     return render(request, template)