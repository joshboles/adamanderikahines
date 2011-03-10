from django.contrib import admin
from rsvp.models import *

class DinnerInline(admin.TabularInline):
    model = DinnerChoice

class DinnerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dinner_choice"]

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["email", "dinner_dancing"]
    list_filter = ["dinner_dancing",]
    inlines = [DinnerInline,]

admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(DinnerChoice, DinnerAdmin)