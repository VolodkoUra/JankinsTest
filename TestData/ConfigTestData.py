import json


class ConfigTestData:
    """
    Класс для получения тестовы данных
    """

    @staticmethod
    def parser_config(param):
        with open('TestData/test_data.json') as file:
            data = json.loads(file.read())
            return data[f'{param}']
