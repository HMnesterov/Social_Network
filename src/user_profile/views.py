from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user.models import Person


@login_required
def user_profile(request, id):
    user = get_object_or_404(Person, id=id)
    try:
        posts = user.where_published.all().select_related('author')
    except AttributeError:
        posts = None
    return render(request, 'profile/profile.html', {'user': user, 'posts': posts})


@login_required
def user_profile_friends(request, id):
    user = get_object_or_404(Person, id=id)
    try:
        friends = user.friends.all()
        return render(request, 'profile/friends.html', {'user': user, 'friends': friends})
    except AttributeError:
        return render(request, 'profile/friends.html', {'user': user, 'friends': None})


@login_required
def show_all_users(request):
    friends = request.user.friends.all()
    return render(request, 'all_users.html', {'users': Person.objects.all(), 'friends': friends})
