from channels.generic.websocket import AsyncWebsocketConsumer


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        print ('connect :v ')
        if self.scope['user'].id:
            await self.accept()
            await self.channel_layer.group_add("cambios", self.channel_name)
            print(f"Added {self.channel_name} channel to cambios")

    async def disconnect(self, close_code):
        if self.scope['user'].id:
            await self.channel_layer.group_discard("cambios", self.channel_name)
            print(f"Removed {self.channel_name} channel to cambios")

    ## envio de los mensajes
    async def cambios(self, event):
        print(f"cambios: {event}")
        await self.send(event)
        print(f"Got message {event} at {self.channel_name}")
