from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^edit/$", "idios.views.profile_edit", name="profile_edit"),
    url(r"^list/$", "idios.views.profiles", name="profile_list"),
    url(r"^(?P<username>[\w\._-]+)/$", "idios.views.profile", name="profile_detail"),
)