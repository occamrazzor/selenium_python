import pytest


# Note: dataLoad is passed to def editProfile as parameter because it is returning data see conftest.py

@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_editProfile(self, data_load):
        print(data_load)
        print(data_load[0])
        print(data_load[2])
