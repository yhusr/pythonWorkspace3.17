from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_request import HandleRequest
from scripts.handle_os import PERSONPHONE_PATH


class HandlePhone:

    @classmethod
    def generate_phone(cls, reg_name, pwd='12345678', reg_type=1):
        hr = HandleRequest()
        hm = HandleMysql()
        phone = hm.get_no_exist_phone()
        header = hy.read_yaml('request', 'header')
        hr.common_head(header)
        data = {"mobile_phone": phone, "pwd": pwd, 'type': reg_type, 'reg_name': reg_name}
        value_result = hr.send(url=hy.read_yaml('register', 'url'), data=data)
        result_phone = value_result.json()['data']['mobile_phone']
        person_result = {reg_name: {"mobile_phone": result_phone, 'pwd': pwd, "type": reg_type, "reg_name": reg_name}}
        hr.close()
        hm.close()
        return person_result

    @classmethod
    def loop_generate_phone(cls):
        hail = HandleYaml(PERSONPHONE_PATH)
        admin_value = cls.generate_phone(reg_name="admin", reg_type=0)
        investor_value = cls.generate_phone(reg_name="investor")
        investor_value.update(admin_value)
        browser_value = cls.generate_phone(reg_name='browser')
        browser_value.update(investor_value)
        hail.write_phone_yaml(browser_value)


if __name__ == '__main__':
    HandlePhone.loop_generate_phone()
