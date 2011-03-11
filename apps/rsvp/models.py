from django.db import models
from model_utils.models import TimeStampedModel

class Rsvp(TimeStampedModel):
    dinner_dancing = models.BooleanField("Will you be joining us for Dinner & Dancing on June 3rd?")
    email = models.EmailField()
    comments = models.TextField(blank=True, null=True)

class DinnerChoice(TimeStampedModel):
    DINNER_CHOICES = (
        (None, "-----"),
        ("turkey", "Stuffed Turkey Roulade"),
        ("salmon", "Citrus Grilled Salmon"),
    )
    rsvp = models.ForeignKey(Rsvp)
    name = models.CharField(max_length=64)
    dinner_choice = models.CharField(max_length=16, choices=DINNER_CHOICES, default=None, null=True)
    
    @property
    def email(self):
        return self.rsvp.email