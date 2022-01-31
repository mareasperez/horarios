"""
ASGI config for config project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "horarios.settings")
django.setup()
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from apps.websocket.consumers import Consumer
from django.urls import path
from apps.mymid.authmid import JwtAuthMiddlewareStack


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            JwtAuthMiddlewareStack(
                URLRouter(
                    [
                        # path(),your routes here
                        path("ws/", Consumer.as_asgi()),
                    ]
                )
            ),
        ),
    }
)
