from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SattingDrivers.SingletonDrivers import Drivers
from TestData.ConfigTestData import ConfigTestData


class Frame:
    """
    Класс для фреймов
    """

    def __init__(self, locator):
        self.locator = locator

    # Поиск элемента
    def find_element(self):
        return WebDriverWait(Drivers.get_driver(), ConfigTestData.parser_config('time')).until(
            EC.presence_of_element_located(self.locator),
            message=f"Can't find element by locator {self.locator}")
