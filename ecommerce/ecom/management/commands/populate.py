from django.core.management.base import BaseCommand, CommandError
from fake_db import FakeDB

class Command(BaseCommand):
    help = 'Fill database with fake data'

    def handle(self, *args, **options):
        print('populating...')
        fake = FakeDB()
        fake.clean_catalog()
        fake.populate_catalog()
        print('populated!')