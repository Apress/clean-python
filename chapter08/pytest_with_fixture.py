import pytest


@pytest.fixture
def get_instance():
    s = CallClassBeforeStartingTest()
    s.call_function()
    return s


@pytest.fixture(scope='session')
def test_data():
    return {"test_data": "This is test data which will be use in different test methods"}


def test_simple(test_data, get_instance):
    assert test_instance.call_another_function(test_data) is not None
