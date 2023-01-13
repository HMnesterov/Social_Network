from django.urls import path
from .views import user_profile, user_profile_friends, post_like_button, user_profile_edit

urlpatterns = [

    path('profile/<int:id>', user_profile, name='user_profile'),
    path('profile/<int:id>/friends', user_profile_friends, name='user_friends'),
    path('profile/likes/<int:post_id>', post_like_button, name='like_post'),
    path('profile/<int:id>/edit', user_profile_edit, name='user_profile_edit')
    ]