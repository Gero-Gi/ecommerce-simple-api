from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Fill database with fake data'

    def handle(self, *args, **options):
        print('Working!')