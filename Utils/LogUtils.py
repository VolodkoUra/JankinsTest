from loguru import logger


class LogUtils:
    def my_loger(self, text):
        logger.add('task_3.log', format="{time} {level} {message}", level="INFO")
        logger.info(text)

    def my_loger_debug(self, text):
        logger.add('task_3.log', format="{time} {level} {message}", level="DEBUG")
        logger.debug(text)

    def my_loger_error(self, text):
        logger.add('task_3.log', format="{time} {level} {message}", level="ERROR")
        logger.error(text)
