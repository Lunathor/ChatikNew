from django.shortcuts import render

from chat.models import Chat

# Create your views here.
def main_view(request):
    # if request not authorized, redirect
    chat_id = None
    context = {
        "chats": Chat.objects.filter(users__in=[request.user.id]),
        # "active_chat": Chat.objects.get(id=chat_id) # or None
    }

    return render(request, 'main.html', context)

# is_user_in_chat = chat.users.filter(id=user_id).exists()