"""View functions for runconf pages."""

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def config_view(request: HttpRequest) -> HttpResponse:
    """View that renders the configuration selection and display page."""
    # Dummy data for DAQ versions and sessions
    daq_versions = ["v1.0.0", "v1.1.0", "v1.2.0"]
    sessions = ["Session A", "Session B", "Session C"]

    # Dummy configuration data
    selected_config = {
        "name": "Default Config",
        "description": "Example configuration for demonstration",
        "daq_version": "v1.0.0",
        "session": "Session A",
        "parameters": {
            "detector_config": "Standard",
            "trigger_mode": "Auto",
            "data_rate": "1 GB/s",
        },
    }

    context = {
        "daq_versions": daq_versions,
        "sessions": sessions,
        "selected_config": selected_config,
    }

    return render(request=request, template_name="runconf/config_view.html", context=context)
