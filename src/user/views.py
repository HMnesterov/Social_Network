from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import Person
from .forms import RegisterUserForm, LoginUserForm


def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You already have an account!')
    form = RegisterUserForm()
    if request.method == 'POST':

        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)

            return HttpResponse('well done')

    return render(request, 'user/register.html', {'form': form})


def authorization(request):
    if request.user.is_authenticated:
        return HttpResponse('You already in your account!')
    form = LoginUserForm()

    if request.method == "POST":

        form = LoginUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)

            return HttpResponse('success')

    return render(request, 'user/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


