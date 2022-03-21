from selenium.webdriver import ActionChains
from PageObjects.BasePage import BasePage
from SattingDrivers.SingletonDrivers import Drivers


class LeftMenuForm(BasePage):
    """
    Класс формы для работы с меню, находящегося слева
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Кнопки меню, находящегося слева
    def buttons_left_pannel(self):
        action = ActionChains(Drivers.get_driver())
        element = self.locator.find_element()
        action.move_to_element(element).perform()
        Drivers.get_driver().execute_script("return arguments[0].scrollIntoView(true);",
                                            self.locator.find_element())
        button = self.locator.find_element()
        button.click()
