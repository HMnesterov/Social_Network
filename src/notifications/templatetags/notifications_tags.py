from django import template

from notifications.models import Notification

register = template.Library()




@register.simple_tag()
def get_last_notifications(request):
    objects = list(request.user.notifications.all())

    class Info:
        def __init__(self, objects):
            self.objects = objects
            self.count = len(self.objects)

    object = Info(objects[-3:] )
    return object