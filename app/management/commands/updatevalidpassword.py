from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Command for updating password as load by fixture.Run this command once the initial data loaded by fixture"

    def handle(self, *args, **options):
        with transaction.atomic():
            for user in User.objects.all():
                if not user.is_superuser:
                    user.set_password(user.password)
                    user.save()