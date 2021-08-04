from django.contrib.auth.models import Group

from rest_framework import status

from catalog_system.constants import Roles
from user.tests.factories import UserFactory
from catalog_system.user.tests.fixtures import authenticate  # noqa: F401;


def test_permissions_users(client, authenticate, subtests):  # noqa: F811;

    scenarios = [
        ("/user/me/", client.get, Roles.ADMIN, {}, status.HTTP_200_OK),
        ("/user/me/", client.get, None, {}, status.HTTP_401_UNAUTHORIZED),
        ("/user/", client.get, Roles.ADMIN, {}, status.HTTP_200_OK),
        ("/user/", client.get, None, {}, status.HTTP_401_UNAUTHORIZED),
    ]

    for ix, (path, method, role, data, response_code) in enumerate(scenarios):
        with subtests.test(msg=f"{path}->{method.__name__}", i=ix):
            if role:
                user = UserFactory(groups=[Group.objects.get(name=role)])
                headers = authenticate(
                    email=user.email, password=user.password_plain_text
                )
                response = method(
                    path, data, content_type="application/json", **headers
                )
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code
