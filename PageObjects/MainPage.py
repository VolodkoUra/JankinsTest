from loguru import logger
from selenium.webdriver.common.by import By
from Elements.Banners import Banners
from Elements.Button import Button
from Forms.LeftMenuForm import LeftMenuForm
from Forms.MainButtonForm import MainButtonForm
from PageObjects.BasePage import BasePage
from Utils.LogUtils import LogUtils


class MainPage(BasePage):
    """
    Класс страницы Main
    """

    # Эелемент кнопки "Alerts, Frame Windows"
    button_alerts_forms_window_element = Button((By.XPATH, "//div[@class='card-body']//*[contains(text(), 'Windows')]"))

    # Эелемент кнопки "Widgets"
    button_widgets_element = Button((By.XPATH, "//div[@class='card-body']//*[contains(text(), 'Widgets')]"))

    # Эелемент кнопки "Elements"
    button_elements = Button((By.XPATH, "//div[@class='card-body']//*[contains(text(), 'Elements')]"))

    # Эелемент кнопки "Browser Windows"
    button_browser_windows_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-0']"))

    button_links_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-5']"))

    # Эелемент кнопки "Slider"
    button_slider_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-3']"))

    # Эелемент кнопки "Progress Bar"
    button_progress_bar_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-4']"))

    button_elements_left_menu = Button((By.XPATH, "//div[@class='header-wrapper']//*[contains(text(), 'Elements')]"))

    def __init__(self):
        self.uniq_element_main_page = Banners((By.XPATH, "//img[@class='banner-image']"))
        super().__init__(self.uniq_element_main_page, 'MainPage')

    # Функция нажатия кнопки "Alerts, Frame Windows" которая скрыта за банером
    @logger.catch
    def click_alerts(self):
        logger = LogUtils()
        logger.my_loger("Нажатиа кнопка 'Alerts, Frame Windows' которая скрыта за банером")
        button_alerts = MainButtonForm(self.button_alerts_forms_window_element, 'MainPage')
        button_alerts.click_button()

    # Функция нажатия кнопки "Widgets" которая скрыта за банером
    @logger.catch
    def click_widgets(self):
        logger = LogUtils()
        logger.my_loger("Нажатиа кнопка 'Widgets' которая скрыта за банером")
        button_alerts = MainButtonForm(self.button_widgets_element, 'MainPage')
        button_alerts.click_button()

    # Функция нажатия кнопки "Elements" которая скрыта за банером
    @logger.catch
    def click_elements(self):
        logger = LogUtils()
        logger.my_loger("Нажатиа кнопка 'Elements' которая скрыта за банером")
        button_elements = MainButtonForm(self.button_elements, 'MainPage')
        button_elements.click_button()

    # Кнопка "Browser Windows" меню слева
    @logger.catch
    def button_browser_windows(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'Browser Windows' меню слева")
        browser_windows = LeftMenuForm(self.button_browser_windows_element, "BrowserWindowsPage")
        browser_windows.buttons_left_pannel()

    # Кнопка "Elements" меню слева
    @logger.catch
    def button_elements_click(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'Elements' меню слева")
        button_elements = LeftMenuForm(self.button_elements_left_menu, 'BrowserWindowsPage')
        button_elements.buttons_left_pannel()

    # Кнопка "Elements --> Links" меню слева
    @logger.catch
    def button_links_click(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'Elements --> Links' меню слева меню слева")
        button_elements = LeftMenuForm(self.button_links_element, 'BrowserWindowsPage')
        button_elements.buttons_left_pannel()

    # Кнопка "Slider" меню слева
    @logger.catch
    def button_slider_click(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'Slider' меню слева меню слева")
        button_elements = LeftMenuForm(self.button_slider_element, 'BrowserWindowsPage')
        button_elements.buttons_left_pannel()

    # Кнопка "Progress Bar" меню слева
    @logger.catch
    def button_progress_bar_click(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'Progress Bar' меню слева меню слева")
        button_elements = LeftMenuForm(self.button_progress_bar_element, 'ProgressBarPage')
        button_elements.buttons_left_pannel()
