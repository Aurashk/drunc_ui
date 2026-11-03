"""Tests for runconf page views."""

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
class TestConfigView:
    """Test the configuration selection view."""

    def test_config_view_requires_login(self) -> None:
        """Test that config view requires authentication."""
        client = Client()
        response = client.get(reverse("runconf:config_view"))
        assert response.status_code == 302  # Redirect to login
        assert "login" in response.url

    def test_config_view_authenticated_user(self) -> None:
        """Test that authenticated user can access config view."""
        user = User.objects.create_user(username="testuser", password="testpass")
        client = Client()
        client.force_login(user)
        response = client.get(reverse("runconf:config_view"))
        assert response.status_code == 200

    def test_config_view_uses_correct_template(self) -> None:
        """Test that config view uses the correct template."""
        user = User.objects.create_user(username="testuser", password="testpass")
        client = Client()
        client.force_login(user)
        response = client.get(reverse("runconf:config_view"))
        assert "runconf/config_view.html" in [t.name for t in response.templates]

    def test_config_view_context_data(self) -> None:
        """Test that config view provides required context variables."""
        user = User.objects.create_user(username="testuser", password="testpass")
        client = Client()
        client.force_login(user)
        response = client.get(reverse("runconf:config_view"))
        context = response.context
        assert "daq_versions" in context
        assert "sessions" in context
        assert "selected_config" in context
        assert len(context["daq_versions"]) > 0
        assert len(context["sessions"]) > 0
