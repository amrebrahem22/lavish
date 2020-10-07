from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = 'this command to create facilities'

    # to add argument
    def add_arguments(self, parser):
        pass
        # parser.add_argument(
        #     '--times', help="Tell me how many time should i tell you I Love You")

    def handle(self, *args, **options):
        facilities = [
            'Private enterance',
            'Paid parking on premises',
            'Paid parking off premises',
            'Elevator',
            'Parking',
            'Gym'
        ]

        for f in facilities:
            Facility.objects.create(name=f)

        self.stdout.write(self.style.SUCCESS(
            f'{len(facilities)} Facilities Created Successfully.'))
