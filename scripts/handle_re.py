import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import HandleYaml
from scripts.handle_os import PERSONPHONE_PATH


class HandleRe:

    @classmethod
    def get_data(cls, data):
        hl = HandleYaml(PERSONPHONE_PATH)
        if re.search("{no_exist_phone}", data):
            hm = HandleMysql()
            result_value = re.sub("{no_exist_phone}", hm.get_no_exist_phone(), data)
            hm.close()
            return result_value
        if re.search("{invest_phone}", data):
            result_value = re.sub("{invest_phone}", hl.read_yaml('investor', 'mobile_phone'), data)
            return result_value
        if re.search("{user_id_re}", data):
            result_value = re.sub("{user_id_re}", str(hl.read_yaml('investor', 'id')), data)
            return result_value
        if re.search('{member_id_re}', data):
            result_value = re.sub("{member_id_re}", str(hl.read_yaml('browser', 'id')), data)
            return result_value
        if re.search("{borrow_phone}", data):
            result_value = re.sub("{borrow_phone}", hl.read_yaml('browser', 'mobile_phone'), data)
            return result_value
        if re.search("{admin_phone}", data):
            result_value = re.sub("{admin_phone}", hl.read_yaml('admin', 'mobile_phone'), data)
            return result_value
        if re.search("{load_id}", data):
            result_value = re.sub("{load_id}", str(getattr(cls, 'item_id')), data)
            return result_value
        if re.search(r"{loan_id_re}", data):
            loan_id_str = str(getattr(HandleRe, 'verify_loan_id'))
            my_value = re.sub('{loan_id_re}', loan_id_str, data)
            result_value = re.sub(r"{user_id}", str(hl.read_yaml('investor', 'id')), my_value)
            return result_value
        return data
