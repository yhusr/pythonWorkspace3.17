import pymysql
import random

from scripts.handle_conf import hy


class HandleMysql:

    def __init__(self):
        self.conn = pymysql.connect(host=hy.read_yaml('mysql', 'host'),
                                    user=hy.read_yaml('mysql', 'user'),
                                    password=hy.read_yaml('mysql', 'password'),
                                    port=hy.read_yaml('mysql', 'port'),
                                    charset='utf8',
                                    db=hy.read_yaml('mysql', 'db'),
                                    cursorclass=pymysql.cursors.Cursor)
        self.cursor = self.conn.cursor()

    # 自由获取手机号
    def get_phone(self):
        return hy.read_yaml('mysql', 'pre_phone')+''.join(random.sample('0123456789', 8))

    # 获取数据库中的数据
    def get_mysql_result(self, sql, args=None, is_one=True):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_one:
            result = self.cursor.fetchone()
        else:
            result = self.cursor.fetchall()
        return result

    # 判断手机号是否在数据库中
    def if_phone_exist(self, phone):
        result = self.get_mysql_result(hy.read_yaml('mysql', 'sql'), args=phone)
        if result:
            return True
        else:
            return False

    # 获取不在数据库中的手机号
    def get_no_exist_phone(self):
        while True:
            phone = self.get_phone()
            if not self.if_phone_exist(phone):
                return phone
                break

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    hm = HandleMysql()
    # result = hm.get_mysql_result(sql=hy.read_yaml('mysql', 'sql'))
    # print(result)
    # phone = hm.get_no_exist_phone()
    # print(phone)
    # result = hm.get_mysql_result(hy.read_yaml('mysql', 'sql'), args=phone)
    # print(result)
    # hm.close()
