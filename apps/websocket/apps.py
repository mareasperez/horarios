from django.apps import AppConfig


class WebsocketConfig(AppConfig):
    name = 'apps.websocket'

    def ready(self):
        pass
        #from . import signals