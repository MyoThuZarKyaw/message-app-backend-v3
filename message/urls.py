from django.urls import path, include
from rest_framework.routers import DefaultRouter

from message.viewsets import Chat_roomViewSet, MessageViewSet

router = DefaultRouter()
router.register('chat_rooms', Chat_roomViewSet, basename='chat_rooms')
router.register('messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]
