from PageObjects.BasePage import BasePage
from TestData.ConfigTestData import ConfigTestData


class ProgressBarForm(BasePage):
    """
    Класс формы для работы c Progress Bar
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Кнопка старт-стоп
    def button_start_click(self):
        self.locator.click()

    # Движение Progress Bar до определённого значения
    def progress_bar_run(self):
        while True:
            if int(self.locator.find_element().get_attribute('aria-valuenow')) == ConfigTestData.parser_config(
                    'age_engineers'):
                self.button_start_click()
                break

    # Текущее значение Progress Bar
    def progress_bar_info(self):
        return int(self.locator.find_element().get_attribute('aria-valuenow'))
