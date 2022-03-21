from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SattingDrivers.SingletonDrivers import Drivers
from TestData.ConfigTestData import ConfigTestData


class BaseElement(ABC):
    """
    Базовый класс для поиска элементов
    """

    def __init__(self, locator):
        self.locator = locator

    # Поиск элемента
    def find_element(self):
        return WebDriverWait(Drivers.get_driver(), ConfigTestData.parser_config('time')).until(
            EC.presence_of_element_located(self.locator),
            message=f"Can't find element by locator {self.locator}")

    # Поиск элемента clickable
    def find_element_to_clickable(self):
        return WebDriverWait(Drivers.get_driver(), ConfigTestData.parser_config('time')).until(
            EC.element_to_be_clickable(self.locator),
            message=f"Can't find element by locator {self.locator}")

    # Поиск списка элементов
    def find_elements(self):
        return WebDriverWait(Drivers.get_driver(), ConfigTestData.parser_config('time')).until(
            EC.presence_of_all_elements_located(self.locator),
            message=f"Can't find elements by locator {self.locator}")

    def click(self):
        self.find_element().click()
