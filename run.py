import pytest
from scripts.handle_os import CASE_PATH, REPORTER_PATH
from libs.HTMLTestRunnerNew import HTMLTestRunner

# class RunTest:
#
#     @staticmethod
#     def run_test():
#
#         suit = unittest.defaultTestLoader.discover(CASE_PATH)
#         runner = HTMLTestRunner(stream=open(REPORTER_PATH, 'wb'),
#                                 description='my_test',
#                                 title='interface_test',
#                                 tester='y.h')
#         runner.run(suit)  # TODO
#

if __name__ == '__main__':
    # RunTest.run_test()
    pytest.main(["-m", "mytest", "--reruns", "1", "--reruns-delay", "1",
                 "--junitxml=reports/allure.xml"])
