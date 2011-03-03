from django.contrib import admin
from rsvp.models import *

class DinnerAdmin(models.TabularInline):
    model = DinnerChoice

class RsvpAdmin(models.ModelAdmin):
    list_display = ["email", "comments"]
    inlines = [DinnerAdmin,]

admin.site.register(Rsvp, RsvpAdmin)