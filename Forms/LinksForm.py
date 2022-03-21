from PageObjects.BasePage import BasePage


class LinksForm(BasePage):
    """
    Класс формы для работы с формой Links
    """

    def __init__(self, locator, name):
        super().__init__(locator, name)

    # Кнопка формы Links
    def button_click(self):
        self.locator.click()
