from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_MALE, "남성"),
        (GENDER_FEMALE, "여성"),
        (GENDER_OTHER, "기타"),
    )

    LANGUAGE_ENGLIGH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICE = ((LANGUAGE_ENGLIGH, "English"), (LANGUAGE_KOREAN, "한국어"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICE = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICE, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
