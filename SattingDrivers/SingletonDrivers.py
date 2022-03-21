from ConfigData.ConfigManager import ConfigManager
from SattingDrivers.WebDriverFactory import WebdriverFactory


class Drivers(object):
    __instance = None
    __driver = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Drivers, cls).__new__(cls)
            cls.__driver = WebdriverFactory.getWebdriver(ConfigManager.parser_config('browser'))
        return cls.__instance

    @staticmethod
    def get_driver():
        if Drivers.__driver is not None:
            return Drivers.__driver
        else:
            Drivers.__driver = WebdriverFactory.getWebdriver(ConfigManager.parser_config('browser'))
        return Drivers.__driver

    @classmethod
    def clean(cls):
        cls.__instance = None

    @staticmethod
    def quit_driver():
        Drivers.clean()
        Drivers.get_driver().quit()
