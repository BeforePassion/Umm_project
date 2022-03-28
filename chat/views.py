from django.http import HttpResponse
from django.shortcuts import redirect, render

from chat.service import create_message, go_chat_room, my_chat_rooms_load


def chat_room_list(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            my_rooms = my_chat_rooms_load(request.user.id)
            return render(request, "chat/chatRoomList.html", {'rooms': my_rooms})
        else:
            return redirect('/')


def chatting_room(request, username):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            my_room = go_chat_room(request.user.id, username)
            return render(request, "chat/chattingRoom.html", {'room': my_room})
        else:
            return redirect('/')
    elif request.method == 'POST':
        user = request.user
        message = request.POST.get('message', '')
        chat_room_id = request.POST.get('chat_room_id', '')
        result = create_message(user, chat_room_id, message)
        return HttpResponse(result)