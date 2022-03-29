from user.models import UserModel
from chat.views import *
from .models import ChatRoom, Message


def go_chat_room(store_user_id, request_user_username):
    user_one = UserModel.objects.filter(id=store_user_id).first()
    user_two = UserModel.objects.filter(username=request_user_username).first()
    if user_one is not None and user_two is not None:
        try:
            chat_room = ChatRoom.objects.filter(
                participants=user_one).filter(participants=user_two).get()
        except ChatRoom.DoesNotExist:
            chat_room = ChatRoom.objects.create()
            chat_room.participants.add(user_one, user_two)
        return chat_room


def my_chat_rooms_load(store_user_id):
    user = UserModel.objects.filter(id=store_user_id).get()
    if user is not None:
        chatRooms = ChatRoom.objects.filter(participants=user)
        return chatRooms


def create_message(user, chat_room_id, message):
    current_chat_room = ChatRoom.objects.filter(id=chat_room_id).get()
    message = Message.objects.create(
        user=user, chat_room=current_chat_room, message=message)
    return message