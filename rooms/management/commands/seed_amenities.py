from django.core.management.base import BaseCommand
from rooms.models import Amenity

NAME = "amenities"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        amenities = [
            "주방",
            "샴푸",
            "난방",
            "에어컨",
            "세탁기",
            "건조기",
            "무선 인터넷",
            "아침식사",
            "실내 벽난로",
            "옷걸이",
            "다리미",
            "헤어드라이어",
            "노트북 작업 공간",
            "TV",
            "아기 침대",
            "유아용 식탁의자",
            "셀프 체크인",
            "화재경보기",
            "일산화탄소 경보기",
            "욕실 단독 사용",
            "해변과 인접",
            "수변",
            "스키를 탄 채로 출입 가능",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} {NAME} created!"))
