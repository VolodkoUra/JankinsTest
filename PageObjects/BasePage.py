class BasePage:
    """
    Базовый класс для страницы
    """

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    # Функция проверки что страница открыта
    def is_open_page(self):
        pages = self.locator.find_element()
        if pages is not None:
            return True
        return False
