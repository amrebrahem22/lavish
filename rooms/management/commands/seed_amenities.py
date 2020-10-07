from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    help = 'this command tells me I Love You'

    # to add argument
    def add_arguments(self, parser):
        pass
        # parser.add_argument(
        #     '--times', help="Tell me how many time should i tell you I Love You")

    def handle(self, *args, **options):
        amenities = [
            'Kitchen',
            'Heating',
            'Washer',
            'Wifi',
            'Indoor fireplace',
            'Iron',
            'Laptop-friendly workspace',
            'Shampoo',
            'Air conditioning',
            'Dryer',
            'Breakfast',
            'Hangers',
            'Hair dryer',
            'TV',
            'Alarm Clock',
            'Balcony',
            'Bathroom',
            'Bathtub',
            'Bed Linen',
            'Boating',
            'Cable TV',
            'Carbon monoxide detectors',
            'chairs',
            'Sofa',
            'Stereo',
            'Swimming pool',
            'Toilet',
            'Towels',
            'Washer',
            'Smoke detector',
            'Shower',
            'shopping Mall'
        ]

        for a in amenities:
            Amenity.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS('Amenities Created Successfully.'))