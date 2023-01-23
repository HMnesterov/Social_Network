from django import template

from notifications.models import Notification

register = template.Library()




@register.simple_tag()
def get_last_notifications(request):
    objects = list(request.user.notifications.all())[-3:]



    context = {'objects': objects, 'count': len(objects)}
    return context