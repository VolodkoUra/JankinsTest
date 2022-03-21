from PageObjects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class WidgetsForm(BasePage):
    """
    Класс формы для работы c виджетами
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Функция для установки слайдера в рандомное положение
    def slider_in(self, random_slider):
        slider = self.locator.find_element()

        """Считыываем текущее положение слайдера, 
        и скидываем его до 0"""
        for i in range(int(slider.get_attribute('value'))):
            slider.send_keys(Keys.LEFT)

        # Устанавливаем слайдер в рандомное положение
        for i in range(random_slider):
            slider.send_keys(Keys.RIGHT)

    # Функция для считывания значения слайдера
    def count_slider_label(self):
        count_label = int(self.locator.find_element().get_attribute('value'))
        return count_label
