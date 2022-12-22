
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from friendship import urls_friends
from user import urls
from user_profile import urls_profile
from user_profile.views import show_all_users
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(urls)),
    path('friendship/', include(urls_friends)),
    path('', include(urls_profile)),
    path('all', show_all_users),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)