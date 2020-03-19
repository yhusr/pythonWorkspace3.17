import pytest
import json
from scripts.handle_excel import HandleExcel
from scripts.handle_conf import hy
from scripts.handle_re import HandleRe
from scripts.handle_log import logger


@pytest.mark.mytest
@pytest.mark.usefixtures('set_up')
class TestVerify:
    he = HandleExcel('verify')
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
    def test_verify(self, set_up, obj):
        url = hy.read_yaml('excel', 'base_url') + obj.url
        my_method = obj.method
        request_data = HandleRe.get_data(data=obj.data)
        result = set_up[0].send(url=url, method=my_method, data=request_data)
        if obj.caseId == 1:
            login_token = result.json()['data']['token_info']['token']
            set_up[0].common_head({"Authorization": "Bearer " + login_token})
        try:
            assert [obj.expected, obj.msg] == [result.json()['code'], result.json()['msg']]
        except AssertionError as e:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=7, sheet_value='fail')
            logger.error(e)
            raise e
        else:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=7, sheet_value='success')
            if obj.caseId == 2:
                loan_data = json.loads(request_data)
                loan_id = loan_data['loan_id']
                setattr(HandleRe, 'verify_loan_id', loan_id)
            logger.info(f"用例{obj.title}执行通过")
        finally:
            self.he.write_excel(rowid=int(obj.caseId) + 1, colid=8, sheet_value=result.text)


if __name__ == '__main__':
    pass
