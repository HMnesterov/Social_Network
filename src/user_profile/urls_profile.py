from django.urls import path
from .views import user_profile, user_profile_friends

urlpatterns = [

path('profile/<int:id>', user_profile, name='user_profile'),
path('profile/<int:id>/friends', user_profile_friends, name='user_friends')
    ]