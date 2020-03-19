import configparser
import yaml
from scripts.handle_os import YAML_PATH, CONF_PATH


class HandleYaml:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = YAML_PATH

    def read_yaml(self, section_name, option_name):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            read_out = yaml.full_load(f)
        yaml_value = read_out[section_name][option_name]
        return yaml_value

    def write_yaml(self, datas):
        with open(self.filepath, 'a', encoding='utf-8') as f:
            yaml.dump(datas, stream=f, allow_unicode=True)

    def write_phone_yaml(self, datas):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            yaml.dump(datas, stream=f, allow_unicode=True)


hy = HandleYaml()


class HandleConfig:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = CONF_PATH
        self.conf = configparser.ConfigParser()

    def read_config(self, section_name, option_name):
        self.conf.read(self.filepath, encoding="utf-8")
        read_in = self.conf[section_name][option_name]
        try:
            read_value = eval(read_in)
        except Exception as e:
            return read_in
        else:
            return read_value

    def write_config(self, datas):
        for data in datas:
            self.conf[data] = datas[data]
        with open(self.filepath, 'w', encoding='utf-8') as f:
            self.conf.write(f)


if __name__ == '__main__':
    # hy = HandleYaml()
    hc = HandleConfig()
    # value = hy.read_yaml(section_name='excel', option_name='filename')
    # print(value)
    datas = {"mysql": {"host": "register"}}
    # hy.write_yaml(datas)
    # con_value = hc.read_config(section_name='excel', option_name='filepath')
    # print(con_value)
    hc.write_config(datas)