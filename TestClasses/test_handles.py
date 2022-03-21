from loguru import logger
from PageObjects.BrowserWindowsPage import BrowserWindowsPage
from PageObjects.MainPage import MainPage
from TestClasses.test_base import start_setting


class TestHandles:
    @logger.catch
    def test_handles(self, start_setting):
        main = MainPage()
        main_page = main.is_open_page()
        assert main_page, 'Main page is not open'
        # Функция нажатия кнопки "Alerts, Frame Windows" которая скрыта за банером
        main.click_alerts()
        # Кнопка "Browser Windows" меню слева
        main.button_browser_windows()
        browser_windows = BrowserWindowsPage()

        # Кнопка "New TAB"
        browser_windows.button_new_tab()
        # Проверка,что страница "New TAB" открылась

        page_new_tab = browser_windows.is_open_page_new_tab()
        assert page_new_tab, 'Страница "New TAB" не открылась'
        # Закрыть текущую вкладку, и перейти на открытую
        browser_windows.close_new_tab()

