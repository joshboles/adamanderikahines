from django.contrib import admin
from rsvp.models import Rsvp

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["dinner_dancing", "how_many", "names", "stuffed_turkey_roulade", "citrus_grilled_salmon"]

admin.site.register(Rsvp, RsvpAdmin)
