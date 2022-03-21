from PageObjects.BasePage import BasePage
from SattingDrivers.SingletonDrivers import Drivers


class MainButtonForm(BasePage):
    """
    Класс формы кнопок на главной странице
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Функция нажатия кнопки формы
    def click_button(self):
        Drivers.get_driver().execute_script("arguments[0].click();", self.locator.find_element_to_clickable())
