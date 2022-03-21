from loguru import logger
from selenium.webdriver.common.by import By
from Alerts.AlertsWindow import AlertsWindow
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from Forms.AlertsForm import AlertsForm
from PageObjects.BasePage import BasePage
from Forms.LeftMenuForm import LeftMenuForm
from TestData.ConfigTestData import ConfigTestData
from Utils.LogUtils import LogUtils


class Alerts(BasePage):
    """
    Класс страницы Alerts
    """

    # Элемент для кнопки alrts меню, находящегося слева
    button_alerts_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-1']"))
    # Элемент для кнопки "...to see alert"
    button_see_alerts_element = Button((By.ID, 'alertButton'))
    # Элемент для кнопки "...confirm box will appear"
    button_confirm_will_box_apper = Button((By.ID, 'confirmButton'))
    # Элемент для кнопки "...prompt box will appear"
    button_prompt_box_will_appear = Button((By.ID, 'promtButton'))

    __alert_text: str  # Переменная для хранения введённого текста в алерт

    def __init__(self):
        self.uniq_element_alerts_page = TextElement((By.XPATH, "//div[contains(text(),'left to start')]"))
        super().__init__(self.uniq_element_alerts_page, 'AlertsPage')

    @logger.catch
    def button_left_pannel_alerts(self):  # Кнопка alerts меню, находящегося слева
        logger = LogUtils()
        logger.my_loger("Нажата кнопка alerts меню, находящегося слева")
        alerts_button = LeftMenuForm(self.button_alerts_element, 'AlertsPage')
        alerts_button.buttons_left_pannel()

    @logger.catch
    def click_button_to_see_alert(self):  # Кнопка Click Button to see alert формы AlertsForm
        logger = LogUtils()
        logger.my_loger("Нажата кнопка Click Button to see alert формы AlertsForm")
        alerts = AlertsForm(self.button_see_alerts_element, "AlertsPage")
        alerts.click_button()

    # Кнопка On button click, confirm box will appear формы AlertsForm
    @logger.catch
    def click_button_confirm_will_box_apper(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка On button click, confirm box will appear формы AlertsForm")
        alerts = AlertsForm(self.button_confirm_will_box_apper, 'AlertsPage')
        alerts.click_button()

    # Кнопка On button click, prompt box will appear формы AlertsForm
    @logger.catch
    def click_button_prompt_box_will_appear(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка On button click, prompt box will appear формы AlertsForm")
        alerts = AlertsForm(self.button_prompt_box_will_appear, 'AlertsPage')
        alerts.click_button()

    # Проверка что алерт с текстом "You clicked a button" открылся
    @logger.catch
    def alert_you_clicked_button(self):
        logger = LogUtils()
        logger.my_loger("Проверка что алерт с текстом 'You clicked a button' открылся")
        alerts = AlertsWindow()
        search_alert = alerts.alert_on(ConfigTestData.parser_config('you_clicked_a_button'))
        if search_alert is not None:
            return True
        return False

    # Кнопка для нажатия ОК у алертов
    @logger.catch
    def alert_accept(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка ОК у алертов")
        alerts = AlertsWindow()
        alerts.alert_accept()

    # Проверка что алерт с текстом "Do you confirm action?" открылся
    @logger.catch
    def alert_on_confirm_box_will_appear(self):
        logger = LogUtils()
        logger.my_loger("Проверка что алерт с текстом 'Do you confirm action?' открылся")
        alerts = AlertsWindow()
        search_alert = alerts.alert_on(ConfigTestData.parser_config('do_you_confirm_action'))
        if search_alert is not None:
            return True
        return False

    # Проверка что появился текст "You selected Ok" рядом с кнопкой On button click, confirm box will appear
    @logger.catch
    def you_select_ok(self):
        logger = LogUtils()
        logger.my_loger(
            "Проверка что появился текст 'You selected Ok' рядом с кнопкой On button click, confirm box will appear")
        alerts = AlertsForm(self, "AlertsPage")
        select_ok = alerts.you_select_ok()
        if select_ok is not None:
            return True
        return False

    # Проверка что алерт с текстом 'Please enter your name' открылся
    @logger.catch
    def alert_on_prompt_box_will_appear(self):
        logger = LogUtils()
        logger.my_loger("Проверка что алерт с текстом 'Please enter your name' открылся")
        alerts = AlertsWindow()
        search_alert = alerts.alert_on(ConfigTestData.parser_config('please_enter_your_name'))
        if search_alert is not None:
            return True
        return False

    # Ввод текста в алерт с названием 'Please enter your name'
    @logger.catch
    def enter_word(self):
        logger = LogUtils()
        logger.my_loger("Ввели текст в алерт с названием 'Please enter your name'")
        alerts = AlertsWindow()
        self.alert_text = alerts.enter_word(ConfigTestData.parser_config('please_enter_your_name'))

    # Проверка что введённый текст в алерт совпадает с тем, что появился под кнопкой
    @logger.catch
    def compare_text_alert(self):
        logger = LogUtils()
        logger.my_loger("Проверка что введённый текст в алерт совпадает с тем, что появился под кнопкой")
        letters_random = self.alert_text
        alerts = AlertsForm(self, "AlertsPage")
        select_rand = alerts.compare_text_alert()
        letters_random = 'You entered ' + letters_random
        if letters_random == select_rand:
            return True
        return False
