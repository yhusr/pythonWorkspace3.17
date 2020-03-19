import pytest
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_os import PERSONPHONE_PATH


@pytest.fixture(scope="class")
def set_up():
    hr = HandleRequest()
    hm = HandleMysql()
    hl = HandleYaml(PERSONPHONE_PATH)
    hr.common_head(hy.read_yaml('request', 'header'))
    yield hr, hm, hl
    hr.close()
    hm.close()
