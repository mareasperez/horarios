from apps.facultades.models import Facultad
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save,sender=Facultad)
def announce_new_facultad(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"facultad.cambios",
                "event":"New Facultad",
                "facultad":instance.facultad_nombre
                        }
        )
@receiver(post_save,sender=Facultad)
def announce_update_facultad(sender,instance,**kwargs):
        print('se llamo al update')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"facultad.cambios",
                "event":"Update Facultad",
                "facultad":instance.facultad_nombre
                        }
        )
@receiver(post_delete,sender=Facultad)
def announce_del_facultad(sender,instance,**kwargs):
        print('se llamo al delete')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"facultad.cambios",
                "event":"Delete Facultad",
                "facultad":instance.facultad_nombre
                        }
        )


