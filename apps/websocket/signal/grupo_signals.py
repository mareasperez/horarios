from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.grupos.models import Grupo


# {type:"grupo", event:"crud"(solo una letra), data:[ grupoModel, grupoModel... ]}

@receiver(post_save,sender=Grupo)
def announce_new_grupo(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "grupo",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=Grupo)
def announce_update_grupo(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "grupo",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=Grupo)
def announce_del_grupo(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "grupo",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


