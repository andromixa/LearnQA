import requests
from lib.logger import Logger
import allure
from environment import BASE_ENV


class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = 0, cookies: dict = 0):
        with allure.step(f'POST request on "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = 0, cookies: dict = 0):
        with allure.step(f'GET request on "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = 0, cookies: dict = 0):
        with allure.step(f'PUT request on "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = 0, cookies: dict = 0):
        with allure.step(f'DELETE request on "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f'{BASE_ENV.get_base_url()git}{url}'

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')

        Logger.add_response(response)

        return response
