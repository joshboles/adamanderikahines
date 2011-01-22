from django import forms
from form_utils.forms import BetterModelForm

from rsvp.models import Rsvp

class RsvpForm(BetterModelForm):    
    dinner_dancing = forms.TypedChoiceField(coerce=bool,
                       choices=((False, 'No'), (True, 'Yes')),
                       widget=forms.RadioSelect
                    )
    
    class Meta:
        model = Rsvp
        fieldsets = [
            ("", {"fields": 
                ["dinner_dancing", "how_many", "names"], "legend": ""
            }),
            ("If attending please choose number of entres", {
                "fields": ["stuffed_turkey_roulade", "citrus_grilled_salmon"],
                "description": "All entres will be served with side salad, rolls & two side dishes",
                "classes": ["", ""]
            }),
            ("",{"fields":
                ["comments",]
            })
        ]