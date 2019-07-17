from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.websocket.consumers import FacultadConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", FacultadConsumer)
    ])
})