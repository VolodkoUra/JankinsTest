from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from Forms.WigetsForm import WidgetsForm
from PageObjects.BasePage import BasePage
from Utils.RandomUtils import RandomgUtils


class Widgets(BasePage):
    """
    Класс страницы Widgets
    """
    element_slider = Button((By.XPATH, "//input[@class='range-slider range-slider--primary']"))
    element_slider_label = TextElement((By.XPATH, "//div[@class='range-slider__tooltip__label']"))

    def __init__(self):
        self.uniq_element_widgets_page = TextElement((By.ID, 'sliderValue'))
        super().__init__(self.uniq_element_widgets_page, 'WidgetsPage')

    # Функция для установки слайдера в рандомное положение
    def slider_in(self):
        self.random_slider = RandomgUtils.random_slider(self.element_slider)
        f = WidgetsForm(self.element_slider, 'Widgets')
        f.slider_in(self.random_slider)

    # Функция для считывания значения слайдера
    def count_slider_label(self):
        f = WidgetsForm(self.uniq_element_widgets_page, 'Widgets')
        res = f.count_slider_label()
        if res == self.random_slider:
            return True
        return False
