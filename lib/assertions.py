from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not JSON ("{response.text}")'

        assert name in response_dict, f'No "{name}" field in response'
        assert response_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not JSON ("{response.text}")'

        assert name in response_dict, f'No "{name}" field in response'

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not JSON ("{response.text}")'

        for name in names:
            assert name in response_dict, f'No "{name}" field in response'

    @staticmethod
    def assert_status_code(response: Response, code):
        assert response.status_code == code, f'Unexpected status code: {response.status_code}'

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not JSON ("{response.text}")'

        assert name not in response_dict, f'"{name}" field is in response, but it shouldn\'t'

