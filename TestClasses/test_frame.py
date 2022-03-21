from loguru import logger
from PageObjects.FramesPage import Frames
from PageObjects.MainPage import MainPage
from TestData.ConfigTestData import ConfigTestData




class TestFrame:
    @logger.catch
    def test_frame(self, start_setting):
        main = MainPage()
        main_page = main.is_open_page()
        assert main_page, 'Main page is not open'
        frame = Frames()
        # Функция нажатия кнопки "Alerts, Frame Windows" которая скрыта за банером
        main.click_alerts()
        # Кнопка "Nested Frames"
        frame.nested_frames()
        # Проверка что в центре страницы присутствуют надписи "Parent frame"
        parent_frame = frame.nested_frames_parent_frame()
        assert parent_frame == ConfigTestData.parser_config(
            'parent_frame'), 'В центре страницы отсутствуют надписи "Parent frame"'
        # Проверка что в центре страницы присутствуют надписи "Child Iframe"
        child_iframe = frame.nested_frames_child_iframe()
        assert child_iframe == ConfigTestData.parser_config(
            'child_iframe'), 'В центре страницы отсутствуют надписи "Child Iframe"'
