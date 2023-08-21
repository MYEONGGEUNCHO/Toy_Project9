# content of tests/subpackage/conftest.py
import pytest

@pytest.fixture
def mid(order):
    order.append("mid subpackage")