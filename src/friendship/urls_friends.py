from django.urls import path
from .views import send_friendship_request, accept_friendship_request, reject_friendship_request, remove_friendship_request, remove_friend

urlpatterns = [

    path('send_friendship_req/<int:id>', send_friendship_request),
    path('accept_friendship/<int:id>', accept_friendship_request),
    path('reject_friendship/<int:id>', reject_friendship_request),
    path('remove_friendship_req/<int:id>', remove_friendship_request),
    path('remove_friend/<int:id>', remove_friend),
]
