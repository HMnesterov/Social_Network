import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from user.models import Person
from user_profile.forms import PostForm, UserProfileEdit
from user_profile.models import Post


class BaseProfileTemplate:
    @staticmethod
    def determine_user_rights_and_his_relationships_with_page_owner(request, user_id):
        page_owner = get_object_or_404(Person, id=user_id)
        visitor = request.user
        if page_owner == visitor:
            who_is_it = 'You'
            admin = True
        elif visitor in page_owner.friends.all():
            who_is_it = 'Friend'

            # We can add some if in this block(for example, if page owner wants to block others posts on his own page)
            admin = True
        else:
            who_is_it = 'Unknown Person'
            admin = False
        return {'who_is_it': who_is_it, 'admin': admin, 'page_owner': page_owner, 'visitor': visitor}


class UserProfile(BaseProfileTemplate, LoginRequiredMixin, View):
    def get(self, request, id):

        who_is_it, admin, page_owner, visitor = self.determine_user_rights_and_his_relationships_with_page_owner(request, id).values()

        try:
            posts = page_owner.where_published.all().select_related('author').order_by('created_date',
                                                                                       'created_time').reverse()
        except AttributeError:
            posts = None

        form = None
        # Detect how request user is related to page owner
        if admin:
            form = PostForm()

        return render(request, 'profile/profile.html',
                      {'user': page_owner,
                       'posts': posts,
                       'post_form': form,
                       'who_is_it': who_is_it})

    def post(self, request, id):
        data = self.determine_user_rights_and_his_relationships_with_page_owner(request, id)
        admin = data['admin']
        if not admin:
            return redirect('user_profile', id=id)

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.where_published = get_object_or_404(Person, id=id)
            form.instance.author = request.user
            form.save()
        return redirect('user_profile', id=id)


@login_required
def user_profile_part_where_we_show_friends(request, id):
    user = Person.objects.prefetch_related('friends').get(id=id)
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
def user_profile_information_edit(request, id):
    page_owner = get_object_or_404(Person, id=id)
    form = UserProfileEdit(initial={'photo': page_owner.photo, 'status': page_owner.status, 'bio': page_owner.bio})
    admin = True if request.user == page_owner else False

    if request.method == "POST":
        form = UserProfileEdit(request.POST, request.FILES)
        if form.is_valid():
            # We place default values to form to make a way to redact already created information
            page_owner.status = form.cleaned_data['status']
            page_owner.bio = form.cleaned_data['bio']
            if form.cleaned_data['photo'] != 'photo':
                page_owner.photo = form.cleaned_data['photo']
            page_owner.save()
            return redirect('user_profile_edit', id=id)
    return render(request, 'profile/edit_profile.html', {'form': form, 'admin': admin, 'user': page_owner})
