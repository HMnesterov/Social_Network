from django.urls import path
from .views import register, authorization, logout_user
from user_profile.views import user_profile

urlpatterns = [

    path('register', register, name='reg'),
    path('auth', authorization, name='login'),
    path('logout', logout_user, name='logout'),
    path('profile/<int:id>', user_profile),

]
