"""URL configuration for runconf app."""

from django.urls import path

from drunc_ui.runconf.views import pages

app_name = "runconf"

urlpatterns = [
    path("config/", pages.config_view, name="config_view"),
]
