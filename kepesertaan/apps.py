from django.apps import AppConfig
import time


class KepesertaanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kepesertaan'

    # def ready(self):
    #     from kepesertaan import telegramBot
    #     telegramBot.start()