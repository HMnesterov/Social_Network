from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import webchat.routing

"""URLS FOR ASGI UPDATE(ASYNC)"""

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            webchat.routing.websocket_urlpatterns
        ),
    ),
})
