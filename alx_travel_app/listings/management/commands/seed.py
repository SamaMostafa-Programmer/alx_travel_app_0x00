import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found to assign as hosts'))
            return

        for i in range(10):
            Listing.objects.create(
                title=f'Sample Listing {i+1}',
                description='This is a sample listing for testing.',
                price_per_night=random.randint(50, 300),
                host=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
