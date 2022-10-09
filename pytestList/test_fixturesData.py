
import pytest

from pytestList.BaseClass import BaseClass


# Note: dataLoad is passed to def editProfile as parameter because it is returning data see conftest.py
# Note: class TestExample2(is passed the parent class...BaseClass) and the import statement above.


@pytest.mark.usefixtures("data_load")
class TestExample2(BaseClass):

    def test_editProfile(self, data_load):
        log = self.getLogger()
        log.info(data_load[0])
        log.info(data_load[2])
        print(data_load[2])
