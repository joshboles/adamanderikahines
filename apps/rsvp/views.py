from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from rsvp.models import Rsvp, DinnerChoice
from rsvp.forms import RsvpForm


def rsvp(request):
    
    # Handles the DinnerChoice
    DinnerChoiceFormset = inlineformset_factory(Rsvp, DinnerChoice, extra=4, can_delete=False)
    formset = DinnerChoiceFormset()

    # Handles the RSVP
    form = RsvpForm(request.POST or None)
    
    if form.is_valid():
        rsvp = form.save()
        
        if rsvp.dinner_dancing:
            # recreate now that we have an instance
            formset = DinnerChoiceFormset(request.POST, instance=rsvp)
            if formset.is_valid():
                formset.save()
            else:
                print formset.errors
        
        messages.success(request, "Your RSVP was received.")
        return redirect("homepage")
    
    return render_to_response("rsvp/form.html", {
        "form": form,
        "formset": formset,
    }, context_instance=RequestContext(request))
