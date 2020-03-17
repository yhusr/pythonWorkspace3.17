from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_request import HandleRequest
from scripts.handle_os import PERSONPHONE_PATH


class HandlePhone:
    hr = HandleRequest()
    hm = HandleMysql()
    hyaml = HandleYaml(PERSONPHONE_PATH)

    def generate_phone(self, reg_name, pwd='12345678', reg_type=1):
        phone = self.hm.get_no_exist_phone()
        header = hy.read_yaml('request', 'header')
        self.hr.common_head(header)
        data = {"mobile_phone": phone, "pwd": pwd, 'type': reg_type, 'reg_name': reg_name}
        value_result = self.hr.send(url=hy.read_yaml('register', 'url'), data=data)
        result_phone = value_result.json()['data']['mobile_phone']
        person_result = {reg_name: {"mobile_phone": result_phone, 'pwd': pwd, "type": reg_type, "reg_name": reg_name}}
        return person_result

    def loop_generate_phone(self):
        admin_value = self.generate_phone(reg_name="admin", reg_type=0)
        self.hyaml.write_yaml(admin_value)
        investor_value = self.generate_phone(reg_name="investor")
        self.hyaml.write_yaml(investor_value)
        browwer_value = self.generate_phone(reg_name='browwer')
        self.hyaml.write_yaml(browwer_value)


if __name__ == '__main__':
    hp = HandlePhone()
    hp.loop_generate_phone()