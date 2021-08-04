from user.models import CatalogUser
from user.tests.factories import UserFactory


def test_user_factories():
    """Test that user factory actually create the object in the test database"""

    user = UserFactory()

    assert CatalogUser.objects.filter(pk=user.pk).exists
