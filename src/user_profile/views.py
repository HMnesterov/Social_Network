from django.shortcuts import render, get_object_or_404

from user.models import Person


def user_profile(request, id):
    user = get_object_or_404(Person, id=id)
    return render(request, 'user/profile.html', {'user': user})
