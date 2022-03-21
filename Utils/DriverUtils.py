from selenium.webdriver.common.alert import Alert
from SattingDrivers.SingletonDrivers import Drivers


class DriverUtils:
    """
    Утилита для работы с драйвером
    """

    # Переход на другой фрейм
    @staticmethod
    def switch_to_frame(frame):
        Drivers.get_driver().switch_to.frame(frame)

    # Переход в новую вкладку
    @staticmethod
    def switch_to_window(tab):
        Drivers.get_driver().switch_to.window(tab)

    # Получить все вкладки
    @staticmethod
    def all_window():
        return Drivers.get_driver().window_handles

    # Закрыть вкладку
    @staticmethod
    def close_window():
        return Drivers.get_driver().close()

    # Кнопка для нажатия ОК у алертов
    @staticmethod
    def alert_accept():
        Alert(Drivers.get_driver()).accept()
