from django.urls import path

from . import views

urlpatterns = [
    path('chat_room_list/', views.chat_room_list, name='chat_room_list'),
    path('chatting_room/<str:username>',
        views.chatting_room, name='chatting_room'),
]
