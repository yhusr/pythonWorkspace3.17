import logging
from scripts.handle_conf import hy
from scripts.handle_os import LOG_FILE_PATH


class HandleLog:

    @staticmethod
    def get_logger():
        logger = logging.getLogger('my_interface_test')
        logger.setLevel(hy.read_yaml("logger", 'level'))
        my_format = hy.read_yaml("logger", 'format')
        formatter = logging.Formatter(my_format)

        # 控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(hy.read_yaml("logger", 'level'))
        sh.setFormatter(formatter)
        logger.addHandler(sh)

        # 文件中输出
        fh = logging.FileHandler(filename=LOG_FILE_PATH, encoding='utf-8')
        fh.setLevel(hy.read_yaml("logger", 'level'))
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger


logger = HandleLog.get_logger()