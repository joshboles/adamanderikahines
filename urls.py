from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "homepage.html"}, name="homepage"),
    # base urls
    url(r"^rsvp/", "rsvp.views.rsvp", name="rsvp"),
    
    url(r"^profiles/", include("profiles.urls")),
    url(r"^blog/", include("biblion.urls")),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^servee/", include("servee.urls")),
    url(r"^frontendadmin/", include("frontendadmin.urls")),
    url(r'^admin_tools/', include('admin_tools.urls')),    
    url(r"^openid/(.*)", PinaxConsumer()),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
