from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import ChatMessage

import json

def index_view(request):
    return render(request, "chat/index.html")

def room_view(request, room_name=None):
    messages = ChatMessage.objects.all().filter(room=room_name)

    chat_text = ""
    for mes in messages:
        chat_text += mes.to_text() + "\\n"

    return render(
        request,
        "chat/room.html",
        {
            "room_name_json": mark_safe(json.dumps(room_name)),
            "chat_text": chat_text
        }
    )
