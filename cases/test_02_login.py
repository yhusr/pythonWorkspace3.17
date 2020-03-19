import pytest

from scripts.handle_excel import HandleExcel
from scripts.handle_conf import hy
from scripts.handle_re import HandleRe
from scripts.handle_log import logger
from scripts.handle_phone import HandlePhone


@pytest.mark.mytest
@pytest.mark.usefixtures('set_up')
class TestLogin:
    he = HandleExcel('login')
    list_obj = he.operate_excel()

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.hr = HandleRequest()
    #     cls.hm = HandleMysql()
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.hr.close()
    #     cls.hm.close()
    @pytest.mark.parametrize('obj', list_obj)
    def test_login(self, set_up, obj):
        url = hy.read_yaml('excel', 'base_url') + obj.url
        # if obj.caseId == 2:
        #     HandlePhone.loop_generate_phone()
        request_data = HandleRe.get_data(data=obj.data)
        result = set_up[0].send(url=url, data=request_data)
        try:
            assert [obj.expected, obj.msg] == [result.json()['code'], result.json()['msg']]
            # self.assertListEqual([obj.expected, obj.msg], [result.json()['code'], result.json()['msg']],
            #                      msg=f"用例{obj.title}执行完成")
        except AssertionError as e:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=7, sheet_value='fail')
            logger.error(e)
            raise e
        else:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=7, sheet_value='success')
            logger.info(f"用例{obj.title}执行通过")
        finally:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=8, sheet_value=result.text)


if __name__ == '__main__':
    pass
