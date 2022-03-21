import pytest
from SattingDrivers.SingletonDrivers import Drivers
from TestData.ConfigTestData import ConfigTestData



def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', help='available browser: chrome, firefox')

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def start_setting(browser):
    driver = Drivers(browser)
    connect = driver.get_driver()
    connect.get(ConfigTestData.parser_config('url'))
    yield
    driver.quit_driver()
