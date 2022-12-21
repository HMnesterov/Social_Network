from django.contrib import admin
from user_profile.models import Post, Property
from .models import Person, Friendship
admin.register(Person)
admin.register(Friendship)
admin.register(Person)
admin.register(Property)