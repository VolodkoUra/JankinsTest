class ConfigManager:
    @staticmethod
    def parser_config(param):
        import json

        with open('ConfigData/config.json') as file:
            data = json.loads(file.read())
            return data[f'{param}']
