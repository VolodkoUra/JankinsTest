from Elements.BaseElement import BaseElement


class TextElement(BaseElement):
    """
    Класс для текстовых элементов
    """

    def __init__(self, locator):
        super().__init__(locator)
