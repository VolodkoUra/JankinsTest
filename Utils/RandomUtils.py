import random
import string
from random import choice
from TestData.ConfigTestData import ConfigTestData


class RandomgUtils:
    """
    Класс для получения рандомного слова,
    определённой длинны, и рандомного значения
    для слайдера
    """

    def random_letters(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(
            choice(letters) for i in range(ConfigTestData.parser_config('count_letters_for_the_random')))
        return rand_string

    # Рандомное значение для слайдера
    @staticmethod
    def random_slider(element_slider):
        max_random = int(element_slider.find_element().get_attribute('max'))
        count_slider = random.randint(0, max_random)
        return count_slider
