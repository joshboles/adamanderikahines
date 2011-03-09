from django.contrib import admin
from rsvp.models import *

class DinnerInline(admin.TabularInline):
    model = DinnerChoice

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["dinner_dancing", "email"]
    inlines = [DinnerInline,]

admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(DinnerChoice)