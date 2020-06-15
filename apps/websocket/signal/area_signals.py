from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.area.models import Area


# {type:"area", event:"crud"(solo una letra), data:[ areaModel, areaModel... ]}

@receiver(post_save, sender=Area)
def announce_new_area(sender, instance, created, **kwargs):
    if created:
        print('se llamo al create')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios", dict(type="cambios", model="area", event="c", data=model_to_dict(instance))
        )


@receiver(post_save, sender=Area)
def announce_update_area(sender, instance, created, **kwargs):
    if not created:
        print('se llamo al update')
        dict_obj = model_to_dict(instance)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios", dict(type="cambios", model="area", event="u", data=model_to_dict(instance))
        )


@receiver(post_delete, sender=Area)
def announce_del_area(sender, instance, **kwargs):
    print('se llamo al delete')
    dict_obj = model_to_dict(instance)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "cambios", dict(type="cambios", model="area", event="d", data=model_to_dict(instance))
    )
