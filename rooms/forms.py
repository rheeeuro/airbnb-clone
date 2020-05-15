from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(label="도시", initial="Anywhere")
    country = CountryField(default="KR").formfield(label="국가")
    room_type = forms.ModelChoiceField(
        label="숙소 유형",
        required=False,
        empty_label="전체",
        queryset=models.RoomType.objects.all(),
    )
    price = forms.IntegerField(required=False, label="가격")
    guests = forms.IntegerField(required=False, label="인원")
    beds = forms.IntegerField(required=False, label="침대 수")
    bedrooms = forms.IntegerField(required=False, label="침실 수")
    baths = forms.IntegerField(required=False, label="욕실 수")
    instant_book = forms.BooleanField(required=False, label="즉시 예약")
    superhost = forms.BooleanField(required=False, label="슈퍼호스트")

    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
