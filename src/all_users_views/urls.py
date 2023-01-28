from django.urls import path
from all_users_views.views import all_users_list_with_dynamic_ajax_update, find_users_by_nickname, news

urlpatterns = [
    path('all_users_list', all_users_list_with_dynamic_ajax_update, name='all_users'),
    path('all_users_list/<slug:text>/', find_users_by_nickname),
    path('', news, name='news'),
]
