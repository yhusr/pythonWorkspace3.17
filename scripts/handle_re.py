import re
from scripts.handle_mysql import HandleMysql


class HandleRe:

    @classmethod
    def get_data(cls, data):
        if re.search("{no_exist_phone}", data):
            hm = HandleMysql()
            result_value = re.sub("{no_exist_phone}", hm.get_no_exist_phone(), data)
            return result_value
        return data
