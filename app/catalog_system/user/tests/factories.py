import names
from uuid import uuid4


def generate_random_user():
    return {
        "email": f"{uuid4()}@zebrands.com",
        "password": "Test123",
        "first_name": names.get_first_name(),
        "last_name": names.get_last_name(),
    }
