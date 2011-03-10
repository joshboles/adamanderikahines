from django import forms
from form_utils.forms import BetterModelForm

from rsvp.models import Rsvp, DinnerChoice

class RsvpForm(BetterModelForm):    
    dinner_dancing = forms.TypedChoiceField(coerce=int,
                       choices=((0, 'No'), (1, 'Yes')),
                       widget=forms.RadioSelect,
                       label="Will you be joining us for Dinner & Dancing on June 3rd?"
                    )
    
    class Meta:
        model = Rsvp
        fieldsets = [
            ("", {"fields": 
                ["dinner_dancing", "email", "comments"], "legend": ""
            }),
        ]

class DinnerChoiceForm(BetterModelForm):
    DINNER_CHOICES = (
        ("turkey", "Stuffed Turkey Roulade"),
        ("salmon", "Citrus Grilled Salmon"),
    )
    def __init__(self, *args, **kwargs):
        super(DinnerChoiceForm, self).__init__(*args, **kwargs)
        self.dinner_choice["widget"] = forms.RadioSelect(choices=DINNER_CHOICES)
    
    class Meta:
        model = DinnerChoice
        fieldsets = [
            ("", {"fields": 
                ["name", "dinner_choice",], "legend": ""
            }),
        ]