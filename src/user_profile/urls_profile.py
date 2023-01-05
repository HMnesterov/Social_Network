from django.urls import path
from .views import user_profile, user_profile_friends, like_button

urlpatterns = [

path('profile/<int:id>', user_profile, name='user_profile'),
path('profile/<int:id>/friends', user_profile_friends, name='user_friends'),
    path('profile/likes/<int:post_id>', like_button, name='like_post')
    ]