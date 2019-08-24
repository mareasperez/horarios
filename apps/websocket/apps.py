from django.apps import AppConfig


class WebsocketConfig(AppConfig):
    name = 'apps.websocket'

    def ready(self):
        pass
        #from . import signals
        from .signal import area_signals
        from .signal import aula_signals
        from .signal import carrera_signals
        from .signal import componente_signals
        from .signal import docente_signals
        from .signal import docenteArea_signals
        from .signal import docenteHora_signals
        from .signal import facultad_signals
        from .signal import grupo_signals
        from .signal import horario_signals
        from .signal import planDeEstudio_signals
        from .signal import planificacion_signals
        from .signal import recinto_signals
        from .signal import departamento_signals