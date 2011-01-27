from django import forms
from form_utils.forms import BetterModelForm

from rsvp.models import Rsvp

class RsvpForm(BetterModelForm):    
    dinner_dancing = forms.TypedChoiceField(coerce=bool,
                       choices=((False, 'No'), (True, 'Yes')),
                       widget=forms.RadioSelect,
                       label="Will you be joining us for Dinner & Dancing on June 3rd?"
                    )
    
    class Meta:
        model = Rsvp
        fieldsets = [
            ("", {"fields": 
                ["dinner_dancing", "how_many", "names"], "legend": ""
            }),
            ("If attending please choose number of entrees", {
                "fields": ["stuffed_turkey_roulade", "citrus_grilled_salmon"],
                "description": "All entrees will be served with side salad, rolls & two side dishes",
                "classes": ["", ""]
            }),
            ("",{"fields":
                ["comments",]
            })
        ]