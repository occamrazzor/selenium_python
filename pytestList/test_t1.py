# All pytest file should start with prefix test_
# pytest method names should start with test
# Any code should be wrapped in method
# To output the console content of the test ie.'Occam' use >py.test -v -s
# pytest treats every function as a testcase
# Always write meaningful name to testcase methods
# To run specific tests that contain CreditCard --- >py.test -k CreditCard -v -s
# Switches -k for specific method name execution, -s log output, -v more info ...metadata
# Mark testcases with @pytest.mark.smoke... precondition import pytest
# To run marked file from CLI > py.test -m smoke -v -s
# @pytest.mark.skip will skip the particular test that is marked
# Include test but skip reporting the result of the test @pytest.mark.xfail
# Fixtures will run setup before test and after test pre-requisite.
# Passing argument of fixture function name to another function see test_t2.py
# any task below yield will be executed last. Example of teardown method.

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print('Occam')

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print('Good Morning')