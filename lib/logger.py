import datetime
import os
from requests import Response


class Logger():
    file_name = f'logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log'

    @classmethod
    def _write_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"""\n-----
Test: {test_name}
Time: {str(datetime.datetime.now())}
Request method: {method}
Request URL: {url}
Request data: {data}
Request headers: {headers}
Request cookies: {cookies}

"""
        cls._write_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_dict = dict(response.cookies)
        headers_dict = dict(response.headers)

        data_to_add = f"""Response code: {response.status_code}
Response text: {response.text}
Response headers: {headers_dict}
Response cookies: {cookies_dict}
-----\n"""
        cls._write_to_file(data_to_add)