from django.core.management.base import BaseCommand
from rooms.models import HouseRule

NAME = "house rules"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        house_rules = ["반려동물 입실 가능", "흡연 가능"]
        for r in house_rules:
            HouseRule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} {NAME} created!"))
