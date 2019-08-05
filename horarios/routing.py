# from django.urls import path
#
# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
#
# from apps.mymid.authmid import TokenAuthMiddlewareStack
#
#
#
# from apps.websocket.consumers import FacultadConsumer
#
# application = ProtocolTypeRouter({
#     "websocket": TokenAuthMiddlewareStack(
#         URLRouter([
#             path("ws/", FacultadConsumer),
#         ]),
#     ),
#
# })
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from apps.websocket.consumers import Consumer
from apps.mymid.authmid import UniversalAuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": UniversalAuthMiddlewareStack(
        URLRouter([
            path("ws/", Consumer),
        ]),
    ),
})