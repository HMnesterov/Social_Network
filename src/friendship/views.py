
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Friendship
from user.models import Person


@login_required
def send_friendship_request(request, id):
    from_user = request.user

    to_user = get_object_or_404(Person, id=id)

    try:
        """ use get_or_created to protect models from dublicate requests"""
        Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)
        return redirect('all_users')
    except AttributeError:
        return HttpResponseBadRequest('404')


@login_required
@transaction.atomic()
def accept_friendship_request(request, id):
    to_user = request.user
    from_user = get_object_or_404(Person, id=id)
    try:
        friend_request = get_object_or_404(Friendship, to_user=to_user, from_user=from_user)
        to_user.friends.add(from_user)
        from_user.friends.add(to_user)
        friend_request.delete()
        return redirect('friendship_requests')
    except AttributeError:
        return HttpResponseBadRequest('404')


@login_required
def reject_friendship_request(request, id):
    to_user = request.user
    from_user = get_object_or_404(Person, id=id)
    try:
        friend_request = get_object_or_404(Friendship, to_user=to_user, from_user=from_user)
        friend_request.delete()
        return redirect('friendship_requests', )
    except AttributeError:
        return HttpResponseBadRequest('404')


@login_required
@transaction.atomic()
def remove_friend(request, id):
    user1 = request.user
    user2 = get_object_or_404(Person, id=id)
    try:
        user1.friends.remove(user2)
        user2.friends.remove(user1)
    except:
        return HttpResponseBadRequest('404')

    return redirect('user_profile', id=id)


@login_required
def show_friendship_requests(request):
    user = request.user
    for_me = user.to_another_user.all()
    return render(request, 'users_list/friend_requests.html', {'requests': for_me})


@login_required
def all_users_list_with_dynamic_ajax_update(request,
               template='users_list/all_users.html',
               page_template='users_list/all_users_page.html'):
    #USERS LIST WITH AJAX UPDATE
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
    serialized_data = [{'username': user.username, 'id': user.id, 'link': user.profile_link(), 'bio': user.bio} for user in users]





    return JsonResponse(serialized_data, safe=False, status=200)

