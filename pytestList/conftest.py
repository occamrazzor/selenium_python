import pytest


# Note @pytest.fixture is common for all test_* files as such will be executed for every
# during runtime. Example would be invoking the browser for every test.
# Scope="class" denotes the test will run once at the top of class level and will run again after all the
# testcase are completed. example cache flush before test run and teardown after all the tests have run.
# fixtures can be used to load data.

@pytest.fixture(scope="class")
def setup():
    print("This is executed first due to pytest fixture()")
    yield
    print('I will be executed last')


@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["occam", "razor", "occam_razor@tester.com"]

# Note create the params parameter and pass the browsers then return the request with params to the calling function
# in test_t1.py.


@pytest.fixture(params=[("chrome","occam","razor"), ("Firefox","razor"), "edge"])

def crossBrowser(request):
    return request.param
