from apps.facultades.models import Facultad
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

# {type:"facultad", event:"crud"(solo una letra), data:[ facultadModel, facultadModel... ]}

@receiver(post_save,sender=Facultad)
def announce_new_facultad(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"facultad",
                "event":"c",
                "facultad": dict_obj
                        }
        )
@receiver(post_save,sender=Facultad)
def announce_update_facultad(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"facultad",
                    "event":"u",
                    "facultad":dict_obj
                            }
            )
@receiver(post_delete,sender=Facultad)
def announce_del_facultad(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"facultad",
                "event":"d",
                "facultad":dict_obj
                        }
        )


