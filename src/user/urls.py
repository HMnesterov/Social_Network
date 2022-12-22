from django.urls import path
from .views import register, authorization, logout_user


urlpatterns = [

    path('register', register, name='reg'),
    path('auth', authorization, name='login'),
    path('logout', logout_user, name='logout'),


]
