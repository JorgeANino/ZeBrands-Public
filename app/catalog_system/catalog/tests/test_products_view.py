from django.contrib.auth.models import Group

from rest_framework import status

from catalog_system.catalog.models import Product
from catalog_system.constants import Roles
from user.tests.factories import UserFactory
from catalog_system.user.tests.fixtures import authenticate  # noqa: F401;

from catalog_system.catalog.tests.factories import ProductFactory


def test_permissions_get_products(client, authenticate, subtests):  # noqa: F811;

    scenarios = [
        ("/product/", client.get, Roles.ADMIN, {}, status.HTTP_200_OK),
        ("/product/", client.get, None, {}, status.HTTP_401_UNAUTHORIZED),
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


def test_permissions_create_products(client, authenticate, subtests):  # noqa: F811;

    valid_product = {
        "sku": "123A",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands",
    }

    scenarios = [
        ("/product/", client.post, Roles.ADMIN, valid_product, status.HTTP_201_CREATED),
        ("/product/", client.post, None, valid_product, status.HTTP_401_UNAUTHORIZED),
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


def test_permissions_update_products(client, authenticate, subtests):  # noqa: F811;

    product = ProductFactory()

    valid_product = {
        "sku": "123A",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands",
    }

    scenarios = [
        (
            f"/product/{product.pk}/",
            client.put,
            Roles.ADMIN,
            valid_product,
            status.HTTP_200_OK,
        ),
        (
            f"/product/{product.pk}/",
            client.put,
            None,
            valid_product,
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
                new_product = Product.objects.get(pk=product.pk)
                assert product.sku != new_product.sku
                assert product.name != new_product.name
                assert product.price != new_product.price
                assert product.brand != new_product.brand
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code


def test_permissions_partial_update_products(
    client, authenticate, subtests   # noqa: F811;
):   # noqa: F811;

    product = ProductFactory()

    valid_product = {
        "sku": "123A",
    }

    scenarios = [
        (
            f"/product/{product.pk}/",
            client.patch,
            Roles.ADMIN,
            valid_product,
            status.HTTP_200_OK,
        ),
        (
            f"/product/{product.pk}/",
            client.patch,
            None,
            valid_product,
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
                new_product = Product.objects.get(pk=product.pk)
                assert product.sku != new_product.sku
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code


def test_permissions_delete_products(client, authenticate, subtests):  # noqa: F811;

    product = ProductFactory()

    scenarios = [
        (
            f"/product/{product.pk}/",
            client.delete,
            Roles.ADMIN,
            {},
            status.HTTP_204_NO_CONTENT,
        ),
        (
            f"/product/{product.pk}/",
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
                new_product = Product.objects.filter(pk=product.pk)
                assert not new_product
            else:
                response = method(path, data, content_type="application/json")
            assert response_code == response.status_code


def test_required_fields_product(client, authenticate, subtests):  # noqa: F811;

    invalid_product = {
        "sku": "123A",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands",
    }

    required_fields_escenarios = ["sku", "name", "price", "brand"]

    user = UserFactory(groups={Group.objects.get(name=Roles.ADMIN)})
    auth_headers = authenticate(email=user.email, password=user.password_plain_text)

    for ix, field in enumerate(required_fields_escenarios):
        with subtests.test(msg="{}".format(field), i=ix):
            bad_item = {**invalid_product}
            bad_item.pop(field)
            error_response = client.post(
                "/product/",
                data=bad_item,
                content_type="application/json",
                **auth_headers,
            )
            assert error_response.data.get(field) == ["This field is required."]
            assert status.HTTP_400_BAD_REQUEST == error_response.status_code
