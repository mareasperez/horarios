from django.apps import AppConfig


class WebsocketConfig(AppConfig):
    name = 'apps.websocket'

    def ready(self):
        from .signal import facultad_signals
        from .signal import  recinto_signals