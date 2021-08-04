import os

import pytest

from django.test import TestCase, TransactionTestCase

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

TestCase.databases = ["default"]
TransactionTestCase.databases = ["default"]


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass
