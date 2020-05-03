from django.core.management.base import BaseCommand
from rooms.models import Facility

NAME = "facilities"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        facilities = ["건물 내 무료 주차", "헬스장", "자쿠지", "수영장"]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} {NAME} created!"))
