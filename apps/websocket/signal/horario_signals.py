from apps.horario.models import Horario
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

# {type:"horario", event:"crud"(solo una letra), data:[ horarioModel, horarioModel... ]}

@receiver(post_save,sender=Horario)
def announce_new_horario(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=Horario)
def announce_update_horario(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "horario",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=Horario)
def announce_del_horario(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "horario",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


