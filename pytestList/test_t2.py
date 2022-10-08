import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = 'occam'
    assert msg == 'hi', 'Test failed due to string mismatch'


def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, 'Addition do not match'

