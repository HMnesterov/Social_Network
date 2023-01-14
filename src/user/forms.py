from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login',)
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Repeat password')
    email = forms.CharField(label='E-mail', )
    photo = forms.ImageField(label='Photo', required=False)

    class Meta:
        model = Person
        fields = ['username', 'password1', 'password2', 'email', 'photo']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', )
    password = forms.CharField(label='Password')

    class Meta:
        model = Person
        fields = ["username", "password"]
