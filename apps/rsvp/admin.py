from django.contrib import admin
from rsvp.models import *

class DinnerAdmin(admin.TabularInline):
    model = DinnerChoice

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["email", "comments"]
    inlines = [DinnerAdmin,]

admin.site.register(Rsvp, RsvpAdmin)