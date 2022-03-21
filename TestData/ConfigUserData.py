import json


class ConfigUserData:
    """
    Класс для плучения данных пользователей,
    для последующей передачи их в тест.
    """

    @staticmethod
    def parser_config_json():
        with open('TestData/users_data.json', 'r') as file:
            result = json.load(file)

        list_users = []
        for i in result.values():
            user = []
            for j in i.values():
                user.append(j)
            list_users.append(user)
        return list_users
