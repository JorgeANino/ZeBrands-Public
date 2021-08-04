import pytest
from types import SimpleNamespace
from user.models import CatalogUser


payload = {"password": "Test123", "email": "test@zebrands.com"}


@pytest.fixture()
def catalog_system_user():
    catalog_system_user = SimpleNamespace(email="user@test.com", password="test123")
    user = CatalogUser.objects.create(email=catalog_system_user.email)
    user.set_password(catalog_system_user.password)
    user.save()
    catalog_system_user.id = user.id
    return catalog_system_user
