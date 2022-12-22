from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Friendship
from user.models import Person


@login_required
def send_friendship_request(request, id):
    from_user = request.user

    to_user = get_object_or_404(Person, id=id)

    try:
        """ use get_or_created to protect models from dublicate requests"""
        Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)
        return redirect('user_profile', id=id)
    except AttributeError:
        return HttpResponseBadRequest('404')



@login_required
def accept_friendship_request(request, id):
    to_user = request.user
    from_user = get_object_or_404(Person, id=id)
    try:
        friend_request = get_object_or_404(Friendship, to_user=to_user,from_user=from_user)
        to_user.friends.add(from_user)
        from_user.friends.add(to_user)
        friend_request.delete()
        return redirect('user_profile', id=id)
    except AttributeError:
        return HttpResponseBadRequest('404')



@login_required
def reject_friendship_request(request, id):
    to_user = request.user
    from_user = get_object_or_404(Person, id=id)
    try:
        friend_request = get_object_or_404(Friendship, to_user=to_user, from_user=from_user)
        friend_request.delete()
        return redirect('user_profile', id=id)
    except AttributeError:
        return HttpResponseBadRequest('404')



@login_required
def remove_friend(request, id):
    user1 = request.user
    user2 = get_object_or_404(Person, id=id)
    try:
       user1.friends.remove(user2)
       user2.friends.remove(user1)
    except:
        return HttpResponseBadRequest('404')

    return redirect('user_profile', id=id)



