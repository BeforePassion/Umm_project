from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
# as_asgi()는 각 사용자 연결에 대해 소비자 인스턴스를 인스턴스화 할 asgi응용 프로그램을 얻기 위해 classmethod를 호출한다. 