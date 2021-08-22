from django.core.management.base import BaseCommand, CommandError
from kepesertaan.telegramBot import start
# from detil_mkro import executor

class Command(BaseCommand):
    help = "Print text Command"

    def handle(self, *args, **options):
        try:
            print('Command is executed')
            start()
            # executor.mulai()
        except Exception as e:
            raise CommandError(e)