from django.urls import path
from .views import view
urlpatterns = [
   path('videochat/', view, name='videochat')
]