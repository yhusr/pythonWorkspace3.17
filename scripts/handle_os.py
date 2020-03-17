import os
import time

current_path = os.path.abspath(__file__)
script_path = os.path.dirname(current_path)
root_path = os.path.dirname(script_path)

# data目录
DATA_PATH = os.path.join(root_path, "data")
EXCEL_PATH = os.path.join(DATA_PATH, "excelcases.xlsx")

# config目录
CONFIG_PATH = os.path.join(root_path, 'config')
YAML_PATH = os.path.join(CONFIG_PATH, 'my_yaml.yaml')
CONF_PATH = os.path.join(CONFIG_PATH, 'my_conf.ini')
PERSONPHONE_PATH = os.path.join(CONFIG_PATH, 'my_phone.yaml')

# logs目录
str_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
LOGS_PATH = os.path.join(root_path, 'logs')
LOG_FILE_PATH = os.path.join(LOGS_PATH, str_time+'.log')

# case目录
CASE_PATH = os.path.join(root_path, 'cases')

# reports目录
REPORT_PATH =os.path.join(root_path, 'reports')
REPORTER_PATH = os.path.join(REPORT_PATH, 'report'+str_time+'.html')
