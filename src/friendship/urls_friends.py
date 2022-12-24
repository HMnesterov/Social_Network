from django.urls import path
from .views import send_friendship_request, accept_friendship_request, reject_friendship_request, remove_friend, show_all_users, show_friendship_requests

urlpatterns = [

    path('send_friendship_req/<int:id>', send_friendship_request, name='friendship_add'),
    path('accept_friendship/<int:id>', accept_friendship_request, name='friendship_accept'),

    path('reject_friendship/<int:id>', reject_friendship_request, name='friendship_reject'),

    path('remove_friend/<int:id>', remove_friend, name='friend_remove'),

    path('all_users_list', show_all_users, name='all_users'),
    path('friendship_requests/', show_friendship_requests, name='friendship_requests')
]
