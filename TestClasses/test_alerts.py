from loguru import logger
from PageObjects.AlertsPage import Alerts
from PageObjects.MainPage import MainPage
from TestClasses.test_base import start_setting


class TestAlerts:
    @logger.catch
    def test_alerts(self, start_setting):
        main = MainPage()
        main_page = main.is_open_page()
        assert main_page, 'Main page is not open'
        main.click_alerts()  # Функция нажатия кнопки "Alerts, Frame Windows" которая скрыта за банером
        alerts = Alerts()
        alerts.button_left_pannel_alerts()  # Кнопка alerts меню, находящегося слева
        alerts.click_button_to_see_alert()  # Кнопка Click Button to see alert формы AlertsForm
        alert_you_click = alerts.alert_you_clicked_button()  # Проверка что алерт с текстом "You clicked a button" открылся
        assert alert_you_click, 'Алерт с текстом "You clicked a button" не открылся'
        alerts.alert_accept()  # Кнопка для нажатия ОК у алертов
        alerts.click_button_confirm_will_box_apper()  # Кнопка On button click, confirm box will appear формы AlertsForm
        alert_confirm = alerts.alert_on_confirm_box_will_appear()  # Проверка что алерт с текстом "Do you confirm action?" открылся
        assert alert_confirm, 'Алерт с текстом "Do you confirm action?" не открылся'
        alerts.alert_accept()
        # Проверка что появился текст "You selected Ok" рядом с кнопкой On button click, confirm box will appear
        select_ok = alerts.you_select_ok()
        assert select_ok, 'Текст "You selected Ok" рядом с кнопкой On button click, confirm box will appear не появился'

        # Кнопка On button click, prompt box will appear формы AlertsForm
        alerts.click_button_prompt_box_will_appear()
        # Проверка что алерт с текстом 'Please enter your name' открылся
        enter_your_name = alerts.alert_on_prompt_box_will_appear()
        assert enter_your_name, "Алерт с текстом 'Please enter your name' не открылся"
        # Ввод текста в алерт с названием 'Please enter your name'
        alerts.enter_word()
        alerts.alert_accept()
        # Проверка что введённый текст в алерт совпадает с тем, что появился под кнопкой
        text_button = alerts.compare_text_alert()
        assert text_button, 'Введённый текст в алерт не совпадает с тем, что появился под кнопкой'
