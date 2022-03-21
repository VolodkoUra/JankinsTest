from loguru import logger
from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.TextElemnt import TextElement
from Forms.WebTablesForm import WebTablesForm
from PageObjects.BasePage import BasePage
from Forms.LeftMenuForm import LeftMenuForm
from TestData.ConfigTestData import ConfigTestData
from Utils.LogUtils import LogUtils


class WebTablesPage(BasePage):
    """
    Класс страницы Web Tables
    """

    # Уникальный элемент страницы Elements
    uniq_element_elements = TextElement((By.XPATH, "//div[contains(text(), 'Please select')]"))
    # Элемент кнопки "Web Tables"
    button_web_tables_element = Button(
        (By.XPATH, "//div[@class='left-pannel']//div[@class='element-list collapse show']//li[@id='item-3']"))
    # Уникальный элемент формы "Web Tables"
    uniq_element_web_tables_form = Button((By.CLASS_NAME, 'pagination-bottom'))
    # Элемент кнопки "ADD"
    button_add_web_tables = Button((By.ID, "addNewRecordButton"))
    # Элементы для ввода данных пользователей
    first_name_field = TextElement((By.ID, "firstName"))
    last_name_field = TextElement((By.ID, "lastName"))
    email_field = TextElement((By.ID, "userEmail"))
    age_field = TextElement((By.ID, "age"))
    salary_field = TextElement((By.ID, "salary"))
    department_field = TextElement((By.ID, "department"))
    # Кнопка "Submit" формы
    button_submit = Button((By.ID, 'submit'))
    # Уникальный элемент самой формы
    uniq_element_web_tables_add = TextElement((By.ID, 'registration-form-modal'))
    # Элемент для проверки, что пользователь добаился в таблицу
    check_dta_submit_element_user_1 = TextElement(
        (By.XPATH, f"//div[@class='rt-td' and contains(text(),'{ConfigTestData.parser_config('first_name_1')}')]"))
    # Элемент для проверки, что пользователь удалился из таблицы
    button_delete_web_tables = Button((By.XPATH, "//div[@class='rt-tr-group' ]//span[@title='Delete']"))

    def __init__(self):
        self.uniq_element_web_tables_form = Button((By.CLASS_NAME, 'pagination-bottom'))
        super().__init__(self.uniq_element_web_tables_form, 'FramePage')

    @logger.catch
    def button_left_pannel_web_tables(self):  # Кнопка web tables меню, находящегося слева
        logger = LogUtils()
        logger.my_loger("Нажата кнопка web tables меню, находящегося слева")
        alerts_button = LeftMenuForm(self.button_web_tables_element, 'WebTablesPage')
        alerts_button.buttons_left_pannel()

    # Проверка, что форма с таблицей открылась
    @logger.catch
    def is_open_page_web_tables_form(self):
        logger = LogUtils()
        logger.my_loger("Проверка, что форма с таблицей открылась")
        base_page = BasePage(self.uniq_element_web_tables_add, 'WebTablesPage')
        return base_page.is_open_page()

    # Проверка, что форма для ввода данных открылась
    @logger.catch
    def is_open_page_web_tables(self):
        logger = LogUtils()
        logger.my_loger("Проверка, что форма для ввода данных открылась")
        base_page = BasePage(self.uniq_element_web_tables_form, 'WebTablesPage')
        return base_page.is_open_page()

    # Проверка, что страница Elements открылась
    @logger.catch
    def is_open_page(self):
        logger = LogUtils()
        logger.my_loger("Проверка, что страница Elements открылась")
        base_page = BasePage(self.uniq_element_elements, 'WebTablesPage')
        return base_page.is_open_page()

    # Кнопка "ADD" формы
    @logger.catch
    def button_add(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'ADD' формы")
        web_tables_form = WebTablesForm(self.button_add_web_tables, "WebTablePage")
        web_tables_form.button_add()

    # Ввод данных пользователей
    @logger.catch
    def enter_word(self, first_name, last_name, email, age, salary, department):
        logger = LogUtils()
        logger.my_loger("Введены данные пользователей")
        f_name = WebTablesForm(self.first_name_field, "WebTablePage")
        f_name.enter_word_field(first_name)
        l_name = WebTablesForm(self.last_name_field, "WebTablePage")
        l_name.enter_word_field(last_name)
        emails = WebTablesForm(self.email_field, "WebTablePage")
        emails.enter_word_field(email)
        ages = WebTablesForm(self.age_field, "WebTablePage")
        ages.enter_word_field(age)
        salarys = WebTablesForm(self.salary_field, "WebTablePage")
        salarys.enter_word_field(salary)
        departments = WebTablesForm(self.department_field, "WebTablePage")
        departments.enter_word_field(department)

    # Кнопка "Submit" формы
    @logger.catch
    def button_submit_click(self):
        logger = LogUtils()
        logger.my_loger("Нажата кнопка 'Submit' формы")
        web_tables_form = WebTablesForm(self.button_submit, "WebTablePage")
        web_tables_form.button_add()

    # Проверка, что пользователь добавился/удалился в таблицу
    @logger.catch
    def check_data_submit(self, first_name):
        logger = LogUtils()
        logger.my_loger("Проверка, что пользователь добавился в таблицу")
        try:
            if TextElement((By.XPATH,
                            f"//div[@class='rt-td' and contains(text(),'{first_name}')]")).find_element() is not None:
                return True
        except:
            return False

    # Удаление пользователя из таблицы
    @logger.catch
    def button_delete(self):
        logger = LogUtils()
        logger.my_loger("Проверка, что пользователь удалился в таблицы")
        web_tables_form = WebTablesForm(self.button_delete_web_tables, "WebTablePage")
        element = web_tables_form.button_delete()[-1]
        element.click()
