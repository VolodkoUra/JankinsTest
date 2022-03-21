from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SattingDrivers.SingletonDrivers import Drivers
from TestData.ConfigTestData import ConfigTestData


class AlertsElement:
    """
    Класс для поиска алертов
    """

    # Поиск аллерта
    @classmethod
    def find_alerts(self, text_alert):
        return WebDriverWait(Drivers.get_driver(), ConfigTestData.parser_config('time')).until(EC.alert_is_present(),
                                                                                               text_alert)
