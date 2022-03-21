from PageObjects.BasePage import BasePage


class WebTablesForm(BasePage):
    """
    Класс формы таблицы
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Кнопка формы Wab Tables
    def button_add(self):
        self.locator.click()

    # Функция ввода данных пользователей
    def enter_word_field(self, word):
        search_field = self.locator.find_element()
        search_field.clear()
        search_field.send_keys(word)

    # Кнопка Delete формы Wab Tables
    def button_delete(self):
        return self.locator.find_elements()
