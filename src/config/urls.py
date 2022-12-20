
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from friendship import urls_friends
from user import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(urls)),
    path('friendship/', include(urls_friends)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)