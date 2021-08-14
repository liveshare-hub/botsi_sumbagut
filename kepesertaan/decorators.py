from accounts.models import ExtendUser

def restricted(func):
    """Restrict usage of func to allowed users only and replies if necessary"""
    # @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.message.chat.id
        qs = ExtendUser.objects.filter(id_telegram=user_id).exists()
        if qs:
            print("WARNING: Unauthorized access denied for {}.".format(user_id))
            update.message.reply_text('User disallowed.')
            return  # quit function
        return func(bot, update, *args, **kwargs)
    return wrapped