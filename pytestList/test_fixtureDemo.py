import pytest


@pytest.fixture()
def setup():
    print("This is executed first due to pytest fixture()")
    yield
    print('I will be executed last')


def test_fixtureDemo(setup):
    print('i will execute steps in fixtureDemo method')
