import requests
from json.decoder import JSONDecodeError

BASE_POINT = 'https://playground.learnqa.ru/api/'


def get_method(endpoint, params):
    return requests.get(BASE_POINT + endpoint, params=params)


def post_method(endpoint, params=None, cookies=None):
    return requests.post(
        BASE_POINT + endpoint,
        data=params if params else None,
        cookies=cookies if cookies else None
    )


payload = {'name': 'Apanas'}

response = get_method('hello/', payload)

try:
    response = response.json()
    key = 'answer'

    if key in response:
        print(response['answer'])
    else:
        print(f'No key {key} in response')
except JSONDecodeError:
    print('Response is not a JSON')

payload = {'login': 'secret_login', 'password': 'secret_pass'}

response = post_method('get_auth_cookie', params=payload)

cookie_val = response.cookies.get('auth_cookie')
cookies = {'auth_cookie': cookie_val} if cookie_val else {}

response_2 = post_method('check_auth_cookie', cookies=cookies)

print(f'{response_2.text}')