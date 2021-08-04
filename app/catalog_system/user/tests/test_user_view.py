from django.contrib.auth.models import Group

from rest_framework import status

from catalog_system.constants import Roles
from user.models import CatalogUser
from user.tests.factories import UserFactory

from catalog_system.user.tests.fixtures import authenticate  # noqa: F401;


def test_get_users_permissions(client, authenticate, subtests):  # noqa: F811;

    scenarios = [
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


def test_create_users_permissions(client, authenticate, subtests):  # noqa: F811;
    new_user = {
        "first_name": "Test Name",
        "last_name": "Test Last",
        "password": "test123456",
        "email": "test@zebrands.com",
    }

    scenarios = [
        ("/user/", client.post, Roles.ADMIN, new_user, status.HTTP_201_CREATED),
        ("/user/", client.post, None, new_user, status.HTTP_401_UNAUTHORIZED),
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


def test_update_user_permissions(client, authenticate, subtests):  # noqa: F811;

    old_user = UserFactory()

    new_user = {
        "first_name": "Test Name",
        "last_name": "Test Last",
        "password": "test123456",
        "email": "test@zebrands.com",
    }

    scenarios = [
        (
            f"/user/{old_user.pk}/",
            client.put,
            Roles.ADMIN,
            new_user,
            status.HTTP_200_OK,
        ),
        (
            f"/user/{old_user.pk}/",
            client.put,
            None,
            new_user,
            status.HTTP_401_UNAUTHORIZED,
        ),
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
                updated_user = CatalogUser.objects.get(pk=old_user.pk)
                assert updated_user.first_name != old_user.first_name
                assert updated_user.last_name != old_user.last_name
                assert updated_user.password != old_user.password
                assert updated_user.email != old_user.email
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code


def test_partially_update_user_permissions(
    client, authenticate, subtests  # noqa: F811;
):  # noqa: F811;

    old_user = UserFactory()

    new_user = {
        "first_name": "Test Name2",
    }

    scenarios = [
        (
            f"/user/{old_user.pk}/",
            client.patch,
            Roles.ADMIN,
            new_user,
            status.HTTP_200_OK,
        ),
        (
            f"/user/{old_user.pk}/",
            client.patch,
            None,
            new_user,
            status.HTTP_401_UNAUTHORIZED,
        ),
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
                updated_user = CatalogUser.objects.get(pk=old_user.pk)
                assert updated_user.first_name != old_user.first_name
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code


def test_delete_user_permissions(client, authenticate, subtests):  # noqa: F811;

    old_user = UserFactory()

    scenarios = [
        (
            f"/user/{old_user.pk}/",
            client.delete,
            Roles.ADMIN,
            {},
            status.HTTP_204_NO_CONTENT,
        ),
        (
            f"/user/{old_user.pk}/",
            client.delete,
            None,
            {},
            status.HTTP_401_UNAUTHORIZED,
        ),
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
                deleted_user = CatalogUser.objects.filter(pk=old_user.pk)
                assert not deleted_user
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code
