from django.contrib import admin

from message.models import Message, Chat_room

# Register your models here.
admin.site.register(Chat_room)
admin.site.register(Message)
