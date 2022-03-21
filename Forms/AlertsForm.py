from selenium.webdriver.common.by import By
from Elements.TextElemnt import TextElement
from PageObjects.BasePage import BasePage


class AlertsForm(BasePage):
    """
    Класс формы для работы c формой для вызова алертов
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Кнопка Click на форме
    def click_button(self):
        self.locator.click()

    # Проверка что появился текст "You selected Ok" рядом с кнопкой On button click, confirm box will appear
    def you_select_ok(self):
        text = TextElement((By.ID, 'confirmResult'))
        select_ok = text.find_element()
        return select_ok

    # Получаем текст который появился под кнопкой
    def compare_text_alert(self):
        text = TextElement((By.ID, 'promptResult'))
        select_rand = text.find_element().text
        return select_rand
