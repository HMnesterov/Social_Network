from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings
from user_profile.views import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('friendship/', include('friendship.urls_friends')),
    path('', include('user_profile.urls_profile')),
    path('', news, name='news'),
    path('chat/', include('webchat.urls_webchat')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
