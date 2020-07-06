from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import blog.routing

# chat : ProtocolTypeRouter route traffic to AuthMiddlewareStack if it sees websocket connection
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            blog.routing.websocket_urlpatterns
        )
    ),
})
