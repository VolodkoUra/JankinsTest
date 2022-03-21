import pytest
from SattingDrivers.SingletonDrivers import Drivers
from TestData.ConfigTestData import ConfigTestData


@pytest.fixture
def start_setting():
    driver = Drivers()
    connect = driver.get_driver()
    connect.get(ConfigTestData.parser_config('url'))
    yield
    driver.quit_driver()
