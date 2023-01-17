from django.urls import path
from .views import UserProfile, user_profile_part_where_we_show_friends, post_like_button, user_profile_information_edit

urlpatterns = [

    path('profile/<int:id>', UserProfile.as_view(), name='user_profile'),
    path('profile/<int:id>/friends', user_profile_part_where_we_show_friends, name='user_friends'),
    path('profile/likes/<int:post_id>', post_like_button, name='like_post'),
    path('profile/<int:id>/edit', user_profile_information_edit, name='user_profile_edit')
    ]