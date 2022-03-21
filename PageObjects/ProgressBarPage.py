from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from Forms.ProgressBarForm import ProgressBarForm
from PageObjects.BasePage import BasePage
from TestData.ConfigTestData import ConfigTestData


class ProgressBar(BasePage):
    """
    Класс страницы Progrss Bar
    """

    progress_bar_info_element = TextElement((By.XPATH, "//div[@class='progress-bar bg-info']"))

    def __init__(self):
        self.button_progress_bar_element = Button((By.ID, 'startStopButton'))
        super().__init__(self.button_progress_bar_element, 'WidgetsPage')

    # Кнопка старт-стоп
    def button_start_progress_bar_click(self):
        progress_bar = ProgressBarForm(self.button_progress_bar_element, 'ProgressBarPage')
        progress_bar.button_start_click()

    # Движение Progress Bar до определённого значения
    def progress_bar_run(self):
        progress_bar = ProgressBarForm(self.progress_bar_info_element, 'ProgressBarPage')
        progress_bar.progress_bar_run()

    # Текущее значение Progress Bar
    def info_progress_bar(self):
        progress_bar = ProgressBarForm(self.progress_bar_info_element, 'ProgressBarPage')
        age = ConfigTestData.parser_config('age_engineers')
        error_age = ConfigTestData.parser_config('error_age')
        min_age = age - error_age
        max_age = age + error_age
        if min_age <= progress_bar.progress_bar_info() <= max_age:
            return True
        return False
