from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from friendship import urls
from user import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(urls)),
    path('friendship/', include(urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)