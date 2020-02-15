from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.componentes.models import Componente


# {type:"componente", event:"crud"(solo una letra), data:[ componenteModel, componenteModel... ]}

@receiver(post_save, sender=Componente)
def announce_new_componente(sender, instance, created, **kwargs):
    if created:
        print('se llamo al create')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios", dict(type="cambios", model="componente", event="c", data=model_to_dict(instance))
        )


@receiver(post_save, sender=Componente)
def announce_update_componente(sender, instance, created, **kwargs):
    if not created:
        print('se llamo al update')
        dict_obj = model_to_dict(instance)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios", dict(type="cambios", model="componente", event="u", data=model_to_dict(instance))
        )


@receiver(post_delete, sender=Componente)
def announce_del_componente(sender, instance, **kwargs):
    print('se llamo al delete')
    dict_obj = model_to_dict(instance)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "cambios", dict(type="cambios", model="componente", event="d", data=model_to_dict(instance))
    )
