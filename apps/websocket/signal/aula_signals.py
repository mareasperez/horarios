from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.aulas.models import Aula


# {type:"aula", event:"crud"(solo una letra), data:[ aulaModel, aulaModel... ]}

@receiver(post_save,sender=Aula)
def announce_new_aula(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "aula",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=Aula)
def announce_update_aula(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "aula",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=Aula)
def announce_del_aula(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "aula",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


