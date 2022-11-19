from django.shortcuts import render


def signup(request):
    template = 'expertises/signup.html'
    return render(request, template)


def registration(request):
    template = 'expertises/registration.html'
    return render(request, template)
