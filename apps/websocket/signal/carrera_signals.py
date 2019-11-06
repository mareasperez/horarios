from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.carreras.models import Carrera


# {type:"carrera", event:"crud"(solo una letra), data:[ carreraModel, carreraModel... ]}

@receiver(post_save,sender=Carrera)
def announce_new_carrera(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "event":"c",
                "model": "carrera",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=Carrera)
def announce_update_carrera(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "carrera",
                    "model": "carrera",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=Carrera)
def announce_del_carrera(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "carrera",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


