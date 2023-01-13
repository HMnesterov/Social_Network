import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from user.models import Person
from user_profile.forms import PostForm, UserProfileEdit
from user_profile.models import Post


@login_required
def user_profile(request, id):
    # Display unique user profile
    user = get_object_or_404(Person, id=id)
    try:
        posts = user.where_published.all().select_related('author').order_by('created_date', 'created_time').reverse()
    except AttributeError:
        posts = None
    if request.user == user or request.user in user.friends.all():  # Detect who is request user for page owner (
        # permission to make a new post)
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
                return redirect('user_profile', id=id)
        return render(request, 'profile/profile.html',
                      {'user': user, 'posts': posts, 'post_form': form, 'who_is_it': who_is_it})
    else:
        return render(request, 'profile/profile.html',
                      {'user': user, 'posts': posts, 'post_form': None, 'who_is_it': 'Unknown person'})


@login_required
def user_profile_friends(request, id):
    user = get_object_or_404(Person, id=id)
    try:
        friends = user.friends.all()
        return render(request, 'profile/friends.html', {'user': user, 'friends': friends})
    except AttributeError:
        return render(request, 'profile/friends.html', {'user': user, 'friends': None})


def news(request):
    if request.user.is_authenticated:

        friends = request.user.friends.all()
        posts = []
        for friend in friends:
            friend_posts = friend.return_posts.all()
            posts += friend_posts

        return render(request, 'news.html', {'posts': posts})
    return render(request, 'news.html')


def count_unique_page_visitors(request):
    pass


def post_like_button(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        post.likes += 1
        post.save()
        ctx = {"likes_count": post.likes, "post_id": post_id}

        return HttpResponse(json.dumps(ctx), content_type='application/json')
    except Exception as e:
        return HttpResponse('Error')


@login_required
def user_profile_edit(request, id):
    #User profile part where owner can edit things like bio and photo
    user = get_object_or_404(Person, id=id)
    form = UserProfileEdit(initial={'photo': user.photo, 'status': user.status, 'bio': user.bio})
    admin = True if request.user == user else False

    if request.method == "POST":
        form = UserProfileEdit(request.POST, request.FILES)
        if form.is_valid():
            user.status = form.cleaned_data['status']
            user.bio = form.cleaned_data['bio']
            if form.cleaned_data['photo'] != 'photo':
                user.photo = form.cleaned_data['photo']
            user.save()
            return redirect('user_profile_edit', id=user.id)
    return render(request, 'profile/edit_profile.html', {'form': form, 'admin': admin, 'user': user})
