from loguru import logger
from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from Frames.Frame import Frame
from PageObjects.BasePage import BasePage
from Forms.LeftMenuForm import LeftMenuForm
from Utils.DriverUtils import DriverUtils
from Utils.LogUtils import LogUtils


class Frames(BasePage):
    """
    Класс страницы Frames
    """

    # Элемент для кнопки "Nested Frames" меню, находящегося слева
    button_nested_frames = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-3']"))
    # Элемент для текста Parent frame
    element_parent_frame = TextElement((By.XPATH, "//body[contains(text(), 'Parent')]"))
    # Элемент для текста Child Iframe
    element_child_iframe = TextElement((By.XPATH, "//*[contains(text(), 'Child Iframe')]"))
    # Фрейм для текста Parent frame
    element_frame_parent = Frame((By.XPATH, '//iframe[@id="frame1"]'))
    # Фрейм для текста Child Iframe
    element_frame_child = Frame((By.XPATH, '//body[contains(text(), "Parent frame")]//iframe'))

    def __init__(self):
        self.uniq_element_frame_page = TextElement((By.XPATH, "//div[contains(text(),'left to start')]"))
        super().__init__(self.uniq_element_frame_page, 'FramePage')

    # Кнопка "Nested Frames"
    @logger.catch
    def nested_frames(self):
        logger = LogUtils()
        logger.my_loger("Нажата Кнопка 'Nested Frames'")
        n_frames = LeftMenuForm(self.button_nested_frames, "FramePage")
        n_frames.buttons_left_pannel()

    # Проверка что в центре страницы присутствуют надписи "Parent frame"
    @logger.catch
    def nested_frames_parent_frame(self):
        logger = LogUtils()
        logger.my_loger("Проверка что в центре страницы присутствуют надписи 'Parent frame'")
        frame = self.element_frame_parent.find_element()
        DriverUtils.switch_to_frame(frame)
        return self.element_parent_frame.find_element().text

    # Проверка что в центре страницы присутствуют надписи "Child Iframe"
    @logger.catch
    def nested_frames_child_iframe(self):
        logger = LogUtils()
        logger.my_loger("Проверка что в центре страницы присутствуют надписи 'Child Iframe'")
        frame = self.element_frame_child.find_element()
        DriverUtils.switch_to_frame(frame)
        return self.element_child_iframe.find_element().text
