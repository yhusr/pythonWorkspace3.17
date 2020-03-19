import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import HandleYaml
from scripts.handle_os import PERSONPHONE_PATH


class HandleRe:

    @classmethod
    def get_data(cls, data):
        if re.search("{no_exist_phone}", data):
            hm = HandleMysql()
            result_value = re.sub("{no_exist_phone}", hm.get_no_exist_phone(), data)
            hm.close()
            return result_value
        if re.search("{invest_phone}", data):
            hy = HandleYaml(PERSONPHONE_PATH)
            result_value = re.sub("{invest_phone}", hy.read_yaml('investor', 'mobile_phone'), data)
            return result_value
        return data
