import pytest


# Note @pytest.fixture is common for all test_* files as such will be executed for every
# during runtime. Example would be invoking the browser for every test.
# Scope="class" denotes the test will run once at the top of class level and will run again after all the
# testcase are completed. example cache flush before test run and teardown after all the tests have run.
@pytest.fixture(scope="class")
def setup():
    print("This is executed first due to pytest fixture()")
    yield
    print('I will be executed last')
