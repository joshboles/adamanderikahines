from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from rsvp.forms import RsvpForm


def rsvp(request):
    form = RsvpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your RSVP was received.")
        return redirect("homepage")
    
    return render_to_response("rsvp/form.html", {
        "form": form,
    }, context_instance=RequestContext(request))
