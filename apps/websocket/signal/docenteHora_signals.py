from apps.docente_horas.models import DocenteHoras
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

# {type:"docente_hora", event:"crud"(solo una letra), data:[ docente_horaModel, docente_horaModel... ]}

@receiver(post_save,sender=DocenteHoras)
def announce_new_docente_hora(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "docente_hora",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=DocenteHoras)
def announce_update_docente_hora(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "docente_hora",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=DocenteHoras)
def announce_del_docente_hora(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "docente_hora",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


