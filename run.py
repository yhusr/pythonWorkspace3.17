import unittest
from scripts.handle_os import CASE_PATH, str_time, REPORTER_PATH
from libs.HTMLTestRunnerNew import HTMLTestRunner


class RunTest:

    @staticmethod
    def run_test():

        suit = unittest.defaultTestLoader.discover(CASE_PATH)
        runner = HTMLTestRunner(stream=open(REPORTER_PATH, 'wb'),
                                description='接口测试',
                                title='interface_test',
                                tester='y.h')
        runner.run(suit)


if __name__ == '__main__':
    RunTest.run_test()