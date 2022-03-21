from loguru import logger
from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from PageObjects.BasePage import BasePage
from Utils.DriverUtils import DriverUtils
from Utils.LogUtils import LogUtils


class BrowserWindowsPage(BasePage):
    """
    Класс страницы Browser Window
    """

    button_new_tab_element = Button((By.ID, "tabButton"))
    uniq_new_tab_element = TextElement((By.ID, "sampleHeading"))

    # Эелемент кнопки "Elements"
    button_elements = Button((By.XPATH, "//div[@class='header-wrapper']//*[contains(text(), 'Elements')]"))
    button_elements_left_menu = Button((By.XPATH, "//div[@class='header-wrapper']//*[contains(text(), 'Elements')]"))

    button_links_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-5']"))

    uniq_links_element = TextElement((By.ID, 'linkWrapper'))
    link_home = Button((By.ID, "simpleLink"))

    def __init__(self):
        self.uniq_element_browser_windows_page = Button((By.ID, "tabButton"))
        BasePage.__init__(self, self.uniq_element_browser_windows_page, 'BrowserWindowsPage')

    # Кнопка "New TAB"
    @logger.catch
    def button_new_tab(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'New TAB' ")
        self.button_new_tab_element.click()

    # Проверка,что страница "New TAB" открылась
    @logger.catch
    def is_open_page_new_tab(self):
        logger = LogUtils()
        logger.my_loger("Проверка,что страница 'New TAB' открылась")
        tab_list = DriverUtils.all_window()
        DriverUtils.switch_to_window(tab_list[1])  # Переход в новую вкладку
        base_page = BasePage(self.uniq_new_tab_element, 'BrowserWindowsPage')
        return base_page.is_open_page()

    # Закрыть текущую вкладку, и перейти на открытую
    @logger.catch
    def close_new_tab(self):
        logger = LogUtils()
        logger.my_loger("Закрыта текущая вкладка, и переход на открытую")
        DriverUtils.close_window()  # закрыть текущую вкладку
        tab_list = DriverUtils.all_window()
        DriverUtils.switch_to_window(tab_list[0])  # Переход в новую вкладку
