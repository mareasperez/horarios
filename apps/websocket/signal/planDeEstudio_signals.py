from apps.plan_de_estudio.models import PlanDeEstudio
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

# {type:"plan_de_estudio", event:"crud"(solo una letra), data:[ plan_de_estudioModel, plan_de_estudioModel... ]}

@receiver(post_save,sender=PlanDeEstudio)
def announce_new_plan_de_estudio(sender,instance,created,**kwargs):
    if created:
        print('se llamo al create')
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "plan_de_estudio",
                "event":"c",
                "data":model_to_dict(instance)
                        }
        )
@receiver(post_save,sender=PlanDeEstudio)
def announce_update_plan_de_estudio(sender,instance,created,**kwargs):
        if not created:
            print('se llamo al update')
            dict_obj = model_to_dict(instance)
            channel_layer= get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "cambios",{
                    "type":"cambios",
                    "model": "plan_de_estudio",
                    "event":"u",
                    "data":model_to_dict(instance)
                            }
            )
@receiver(post_delete,sender=PlanDeEstudio)
def announce_del_plan_de_estudio(sender,instance,**kwargs):
        print('se llamo al delete')
        dict_obj = model_to_dict(instance)
        channel_layer= get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios",{
                "type":"cambios",
                "model": "plan_de_estudio",
                "event":"d",
                "data":model_to_dict(instance)
                        }
        )


