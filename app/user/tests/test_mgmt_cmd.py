from django.contrib.auth import get_user_model
from django.core import management


def test_mgmt_cmd_createsuperuser():
    """Test that createsuperuser management command is working"""
    management.call_command(
        "createsuperuser", interactive=False, email="admin@zebrands.com"
    )
    assert get_user_model().objects.filter(email="admin@zebrands.com").exists()
