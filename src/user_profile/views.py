from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user.models import Person
from user_profile.forms import PostForm


@login_required
def user_profile(request, id):
    user = get_object_or_404(Person, id=id)
    try:
        posts = user.where_published.all().select_related('author').order_by('created_date', 'created_time').reverse()
    except AttributeError:
        posts = None
    if request.user == user or request.user in user.friends.all():
        if request.user == user:
            who_is_it = 'You'
        else:
            who_is_it = 'FRIEND'
        form = PostForm()
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.where_published = user
                form.instance.author = request.user
                form.save()
                form.clean()
        return render(request, 'profile/profile.html', {'user': user, 'posts': posts, 'post_form': form, 'who_is_it': who_is_it})
    else:
        return render(request, 'profile/profile.html', {'user': user, 'posts': posts, 'post_form': None, 'who_is_it': 'Unknown person'})


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
    return render(request, 'all_users.html', {'users': Person.objects.all().exclude(id=request.user.id), 'friends': friends})
