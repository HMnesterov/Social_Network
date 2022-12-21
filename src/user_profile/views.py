from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user.models import Person


@login_required
def user_profile(request, id):
    user = get_object_or_404(Person, id=id)
    try:
        posts = user.where_published.all()

        return render(request, 'user/profile.html', {'user': user, 'posts': posts})
    except AttributeError:
        return render(request, 'user/profile.html', {'user': user, 'posts': None})


