from django.core.management.base import BaseCommand
from myapp.models import Client
class Command(BaseCommand):
    help = "Delete user by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = Client.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')