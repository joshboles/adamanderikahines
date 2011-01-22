from django.db import models
from model_utils.models import TimeStampedModel

class Rsvp(TimeStampedModel):
    dinner_dancing = models.BooleanField("Will you be joining us for Dinner & Dancing on June 3rd?")
    how_many = models.IntegerField("How many will be attending?", blank=True, null=True)
    names = models.CharField("Name or names of who will be attending", max_length=1024, blank=True, null=True)
    stuffed_turkey_roulade = models.IntegerField(default=0, help_text="Sliced turkey breast stuffed with pine nuts, carrots, spinach & red onions. Served with an orange and terragon burgundy sauce.")
    citrus_grilled_salmon = models.IntegerField(default=0, help_text="Grilled salmon fillet with a tri-colored peppercorn citrus sauce.")
    comments = models.TextField("Any Questions or Comments", blank=True, null=True)
