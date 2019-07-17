from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.recintos.models import Recinto


@receiver(post_save,sender=Recinto)
def announce_new_recinto(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model":"recinto",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=Recinto)
def announce_update_recinto(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "recinto",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=Recinto)
def announce_del_recinto(sender,instance,**kwargs):
        print('se llamo al delete')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "recinto",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


