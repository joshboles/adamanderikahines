from django.contrib import admin
from rsvp.models import *

class DinnerInline(admin.TabularInline):
    model = DinnerChoice
    list_display = ["name", "dinner_choice"]

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["dinner_dancing", "email"]
    inlines = [DinnerInline,]

admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(DinnerChoice, DinnerInline)