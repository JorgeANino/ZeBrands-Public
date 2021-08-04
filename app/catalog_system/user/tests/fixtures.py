import pytest


@pytest.fixture()
def authenticate(client):
    def _authenticate(email, password):
        response = client.post(
            "/user/token/", data={"email": email, "password": password}
        )
        return {"HTTP_AUTHORIZATION": "Bearer {}".format(response.data.get("access"))}

    return _authenticate
