from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .fixtures import catalog_system_user  # noqa: F401;


def test_valid_credentials(client, catalog_system_user):  # noqa: F811;
    """Test that token is created with valid credentials"""
    response = client.post(
        "/user/token/",
        data={
            "email": catalog_system_user.email,
            "password": catalog_system_user.password,
        },
    )
    assert response.status_code == 200
    assert "refresh" in response.data
    assert "access" in response.data


def test_invalid_credentials(client, catalog_system_user):  # noqa: F811;
    """Test that token is not created with invalid credentials"""
    response = client.post(
        "/user/token/", data={"email": catalog_system_user.email, "password": "wrongpw"}
    )
    assert response.status_code == 401
    assert (
        response.data.get("detail")
        == "No active account found with the given credentials"
    )


def test_refresh_token_and_invalidation(client, catalog_system_user):  # noqa: F811;
    """Test that refresh token is generated and then invalidated"""
    response = client.post(
        "/user/token/",
        data={
            "email": catalog_system_user.email,
            "password": catalog_system_user.password,
        },
    )
    refresh_token = response.data.get("refresh")

    refreshed_response = client.post(
        "/user/token/refresh/", data={"refresh": refresh_token}
    )
    assert refreshed_response.status_code == 200
    assert "refresh" in refreshed_response.data
    assert "access" in refreshed_response.data

    # Making sure that the refresh token is not valid anymore
    assert OutstandingToken.objects.filter(token=refresh_token).exists()
    invalid_response = client.post(
        "/user/token/refresh/", data={"refresh": refresh_token}
    )
    assert invalid_response.status_code == 401
    assert invalid_response.data.get("detail") == "Token is blacklisted"


def test_refresh_token_and_logout(client, catalog_system_user):  # noqa: F811;
    """Test that refresh token is black listed when logging out"""
    response = client.post(
        "/user/token/",
        data={
            "email": catalog_system_user.email,
            "password": catalog_system_user.password,
        },
    )
    refresh_token = response.data.get("refresh")

    refreshed_response = client.post("/user/logout/", data={"refresh": refresh_token})
    assert refreshed_response.status_code == 200

    # Making sure that the refresh token is not valid anymore
    assert OutstandingToken.objects.filter(token=refresh_token).exists()
    invalid_response = client.post(
        "/user/token/refresh/", data={"refresh": refresh_token}
    )
    assert invalid_response.status_code == 401
    assert invalid_response.data.get("detail") == "Token is blacklisted"
