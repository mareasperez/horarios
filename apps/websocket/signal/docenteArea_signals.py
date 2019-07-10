from apps.docente_area.models import DocenteArea
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

# {type:"docente_area", event:"crud"(solo una letra), data:[ docente_areaModel, docente_areaModel... ]}

@receiver(post_save,sender=DocenteArea)
def announce_new_docente_area(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "docente_area",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=DocenteArea)
def announce_update_docente_area(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "docente_area",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=DocenteArea)
def announce_del_docente_area(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "docente_area",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


