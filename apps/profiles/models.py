from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
from idios.models import ProfileBase
from model_utils import Choices

class Profile(ProfileBase):
    COLOR = Choices(
        ("red", "Red"),
        ("green", "Green"),
        ("blue", "Blue"),
    )
    favorite_color = models.CharField(max_length=12, choices=COLOR,
        default=COLOR.red)