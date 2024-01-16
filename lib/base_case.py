import json.decoder
from datetime import datetime

from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'No {cookie_name} cookie in response'
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f'No {header_name} header in response'
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not JSON ("{response.text}")'

        assert name in response, f'No "{name}" field in response JSON'
        return response[name]

    def prepare_reg_data(self, email=None):
        if email is None:
            base_part = 'learnqa'
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f'{base_part}{random_part}@{domain}'
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

