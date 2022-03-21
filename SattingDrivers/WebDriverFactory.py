from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as chrome_options
from ConfigData.ConfigManager import ConfigManager


class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if browserName == 'chrome':
            options = chrome_options()
            options.add_argument(ConfigManager.parser_config('browser'))
            options.add_argument(ConfigManager.parser_config('start-max'))
            options.add_argument(ConfigManager.parser_config('window-size'))
            options.add_argument(ConfigManager.parser_config('chrome_certificate_errors'))
            options.add_argument("disable-infobars")
            options.add_argument("disable-extensions")
            options.add_argument("disable-gpu")
            options.add_argument("disable-dev-shm-usage")
            options.add_argument("no-sandbox")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            return driver
        elif browserName == 'firefox':
            options = Options()
            options.add_argument(ConfigManager.parser_config('width'))
            options.add_argument(ConfigManager.parser_config('height'))
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            return driver

        raise Exception("No such " + browserName + " browser exists")
