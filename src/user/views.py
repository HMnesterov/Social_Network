from django.shortcuts import render, redirect

from django.contrib.auth import login, logout

from .forms import RegisterUserForm, LoginUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('user_profile', id=request.user.id)
    form = RegisterUserForm()
    if request.method == 'POST':

        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)

            return redirect('user_profile', id=user.id)

    return render(request, 'user/register.html', {'form': form})


def authorization(request):
    if request.user.is_authenticated:
        return redirect('user_profile', id=request.user.id)
    form = LoginUserForm()

    if request.method == "POST":

        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)

            return redirect('user_profile', id=user.id)

    return render(request, 'user/register.html', {'form': form})


def logout_user(request):

    logout(request)
    return redirect('login')


