from django.core.management.base import BaseCommand, CommandError
from kepesertaan.telegramBot import start

class Command(BaseCommand):
    help = "Print text Command"

    def handle(self, *args, **options):
        try:
            print('Command is executed')
            start()
        except Exception as e:
            raise CommandError(e)