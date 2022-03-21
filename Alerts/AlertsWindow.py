from Alerts.AlertsElement import AlertsElement
from Utils.RandomUtils import RandomgUtils
from Utils.DriverUtils import DriverUtils


class AlertsWindow:
    """
    Класс для работы с окнами алертов
    """

    # Проверка что алерт открылся
    def alert_on(self, text):
        search_alert = AlertsElement.find_alerts(text)
        return search_alert

    # Кнопка для нажатия ОК у алертов
    def alert_accept(self):
        DriverUtils.alert_accept()

    # Ввод текста в алерт с названием 'Please enter your name'
    def enter_word(self, text):
        alert = AlertsElement.find_alerts(text)
        chars = RandomgUtils()
        letters_random = chars.random_letters()
        alert.send_keys(letters_random)  # Ввели текст
        return letters_random
