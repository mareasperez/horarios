from channels.routing import ProtocolTypeRouter, URLRouter
from apps.websocket.consumers import FacultadConsumer
from django.urls import path

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", FacultadConsumer)
    ])
})