import unittest

from scripts.handle_excel import HandleExcel
from libs.ddt import data, ddt
from scripts.handle_conf import hy
from scripts.handle_request import HandleRequest
from scripts.handle_re import HandleRe
from scripts.handle_log import logger
from scripts.handle_mysql import HandleMysql


@ddt
class TestRegister(unittest.TestCase):
    he = HandleExcel('register')
    list_obj = he.operate_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.hr = HandleRequest()
        cls.hm = HandleMysql()

    @data(*list_obj)
    def test_register(self, obj):
        url = hy.read_yaml('excel', 'base_url') + obj.url
        self.hr.common_head(hy.read_yaml('request', 'header'))
        request_data = HandleRe.get_data(data=obj.data)
        result = self.hr.send(url=url, data=request_data)
        try:
            self.assertListEqual([obj.expected, obj.msg], [result.json()['code'], result.json()['msg']], msg=f"用例{obj.title}执行完成")
            if obj.caseId == 1:
                phone = result.json()['data']['mobile_phone']
                mysql_result = self.hm.get_mysql_result(hy.read_yaml('mysql', 'sql'), args=phone)
                self.assertIsNotNone(mysql_result)
        except AssertionError as e:
            self.he.write_excel(rowid=int(obj.caseId)+1, colid=7, sheet_value='fail')
            logger.error(e)
            raise e
        else:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=7, sheet_value='success')
            logger.info(f"用例{obj.title}执行通过")
        finally:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=8, sheet_value=result.text)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hr.close()
        cls.hm.close()

