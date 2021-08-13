from accounts.models import ExtendUser


# def login_only(view_func):
#     def wrapper_func(message, *args, **kwargs):
#         group = None
#         user = message.chat.id
#         qs = ExtendUser.objects.get(id_telegram=user)
#         if qs.DoesNotExist:
#             bot.send_message(user, "User anda tidak dikenal. Silahkan Login terlebih dahulu")

#         else:
            
#             return view_func(request, *args, **kwargs)
#     return wrapper_func

def cek_login(bot, message):
    user = message.chat.id
    status = False
    qs = ExtendUser.objects.filter(id_telegram=user)
    if not qs:
       
       return False
    else:
        return True