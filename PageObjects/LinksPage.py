from loguru import logger
from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from Forms.LinksForm import LinksForm
from PageObjects.BasePage import BasePage
from Utils.DriverUtils import DriverUtils
from Utils.LogUtils import LogUtils


class Links(BasePage):
    """
    Класс страницы Links
    """

    button_new_tab_element = Button((By.ID, "tabButton"))
    uniq_new_tab_element = TextElement((By.ID, "sampleHeading"))

    # Эелемент кнопки "Elements"
    button_elements = Button((By.XPATH, "//div[@class='header-wrapper']//*[contains(text(), 'Elements')]"))
    link_home = Button((By.ID, "simpleLink"))

    def __init__(self):
        self.uniq_element_links_page = TextElement((By.ID, 'linkWrapper'))
        super().__init__(self.uniq_element_links_page, 'LinksPage')

    # Ссылка "Home" формы Links
    @logger.catch
    def button_links_home(self):
        logger = LogUtils()
        logger.my_loger("Переход по ссылке 'Home' формы Links")
        links = LinksForm(self.link_home, 'BrowserWindowsPage')
        links.button_click()

    # Перейти на новую вкладку, закрыть её, затем вернуться на предыдущую
    @logger.catch
    def switch_to_new_tab_and_close(self):
        logger = LogUtils()
        logger.my_loger("Переход на новую вкладку, закрыть её, затем вернуться на предыдущую")
        tab_list = DriverUtils.all_window()
        DriverUtils.switch_to_window(tab_list[1])  # Переход в новую вкладку
        DriverUtils.close_window()  # закрыть текущую вкладку
        tab_list = DriverUtils.all_window()
        DriverUtils.switch_to_window(tab_list[0])  # Переход в новую вкладку
