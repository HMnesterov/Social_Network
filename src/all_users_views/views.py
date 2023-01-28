from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from user.models import Person


@login_required
def all_users_list_with_dynamic_ajax_update(request,
                                            template='users_list/all_users.html',
                                            page_template='users_list/all_users_page.html'):
    # USERS LIST WITH AJAX UPDATE
    context = {
        'users': Person.objects.all().exclude(id=request.user.id),
        'friends': request.user.friends.all(),
        'all_users_page': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)


@login_required
def find_users_by_nickname(request, text):
    users = Person.objects.filter(username__icontains=text)
    serialized_data = [{'username': user.username, 'id': user.id, 'link': user.profile_link(), 'bio': user.bio} for user
                       in users]

    return JsonResponse(serialized_data, safe=False, status=200)


def news(request, template='news.html', page_template='profile/tags/posts.html'):
    if request.is_ajax():
        template = page_template

    if request.user.is_authenticated:
        friends = request.user.friends.all()
        posts = []
        for friend in friends:
            friend_posts = friend.return_posts.all()
            posts += friend_posts
        context = {
            'posts': posts,
        }

        return render(request, template, context)
    return render(request, template)