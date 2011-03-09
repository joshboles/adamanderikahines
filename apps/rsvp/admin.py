from django.contrib import admin
from rsvp.models import *

class DinnerAdmin(admin.TabularInline):
    model = DinnerChoice

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["dinner_dancing", "name", "dinner_choice", "email"]
    inlines = [DinnerAdmin,]

admin.site.register(Rsvp, RsvpAdmin)