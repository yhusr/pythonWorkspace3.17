import requests
import json


class HandleRequest:
    def __init__(self):
        self.conn = requests.session()

    def common_head(self, head):
        self.conn.headers.update(head)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except NameError as e:
                data = eval(data)

        method = method.lower()
        if method == 'get':
            response_result = self.conn.request(method=method, url=url, params=data, **kwargs)
        elif method in ('post', 'put', 'patch', 'delete'):
            if is_json:
                response_result = self.conn.request(method=method, url=url, json=data, **kwargs)
            else:
                response_result = self.conn.request(method=method, url=url, data=data, **kwargs)
        else:
            response_result = None
            print(f'此方法{method}没有返回值')
        return response_result

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    hr = HandleRequest()
    result = hr.send(url='http://www.baidu.com', method='get')
    print(result.json())