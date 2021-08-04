import pytest

from user.services import create_user, create_superuser

from .fixtures import payload


def test_create_admin_successful():
    """Test successful creation of new user"""
    user = create_superuser(**payload)

    assert user.email == payload["email"]
    assert user.check_password(payload["password"])


def test_create_admin_invalid_email():
    """Test that an error is raised when creating an user with no email"""
    with pytest.raises(ValueError):
        create_superuser(email=None, password=payload["password"])


def test_create_admin_email_normalize():
    """Test email of new user is normalized"""
    capitalized_email_payload = {
        "email": "test@zebrands.COM",
        "password": "Test123",
    }
    user = create_superuser(**capitalized_email_payload)
    assert user.email == payload["email"].lower()


def test_create_user_not_allowed():
    """Tests that an error is returned when a user is being created"""
    with pytest.raises(ValueError):
        create_user(email=None, password=payload["password"])
