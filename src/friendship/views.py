from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required

from .models import Friendship
from user.models import Person


@login_required
def send_friendship_request(request, id):
    from_user = request.user

    to_user = get_object_or_404(Person, id=id)

    try:
        """ use get_or_created to protect models from dublicate requests"""
        Friendship.objects.get_or_created(from_user=from_user, to_user=to_user)
        return HttpResponse('Friend request is created')
    except:
        return Http404


@login_required
def remove_friendship_request(request, id):
    from_user = request.user

    to_user = get_object_or_404(Person, id=id)

    try:
        friend_request = get_object_or_404(Friendship, from_user=from_user, to_user=to_user)
        friend_request.delete()
        return HttpResponse('Friend request is deleted')
    except:
        return Http404

@login_required
def accept_friendship_request(request, id):
    to_user = request.user
    from_user = get_object_or_404(Person, id=id)
    try:
        friend_request = get_object_or_404(Friendship, to_user=to_user,from_user=from_user)
        to_user.friends.add(from_user)
        from_user.friends.add(to_user)
        friend_request.delete()
        return HttpResponse("New friend is added")
    except:
        return Http404



@login_required
def reject_friendship_request(request, id):
    to_user = request.user
    from_user = get_object_or_404(Person, id=id)
    try:
        friend_request = get_object_or_404(Friendship, to_user=to_user, from_user=from_user)
        friend_request.delete()
        return HttpResponse("Friendship is rejected")
    except:
        return Http404

