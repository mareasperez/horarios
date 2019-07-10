
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class FacultadConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("cambios", self.channel_name)
        print(f"Added {self.channel_name} channel to cambios")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("cambios", self.channel_name)
        print(f"Removed {self.channel_name} channel to cambios")

    ## envio de los mensajes
    async def cambios(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
