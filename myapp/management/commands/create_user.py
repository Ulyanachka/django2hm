from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = Client(name="Ulya", email="ulaaa@example.com", phone_number=123123, address = 'loyalstreet')
        ...
        user.save()
        self.stdout.write(f'{user}')