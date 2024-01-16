import pytest
import requests
from temp import agents
from lib.assertions import Assertions


def test_task_10():
    user_phrase = input('Inter phrase less then 15 symbols long: ')
    frase_length = len(user_phrase)
    assert frase_length < 15, f"It looks like your frase is not less then 15 symbols! It's {frase_length} symbols long"


def test_task_11():
    method_link = 'https://playground.learnqa.ru/api/homework_cookie'
    expected_value = 'hw_value'
    response = requests.get(method_link)
    cookie = response.cookies.get('HomeWork')
    assert cookie == expected_value, 'Cookies verification failed'


def test_task_12():
    method_link = 'https://playground.learnqa.ru/api/homework_header'
    expected_value = 'Some secret value'
    response = requests.get(method_link)
    header = response.headers.get('x-secret-homework-header')
    assert header == expected_value, 'Headers verification failed'

@pytest.mark.parametrize('agent_info', agents)
def test_task_13(agent_info):
    method_link = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
    headers = {"User-Agent": agent_info['user_agent']}
    response = requests.get(method_link, headers=headers)

    for key in agent_info:
        if key == 'user_agent':
            continue
        Assertions.assert_json_value_by_name(
            response,
            key,
            agent_info[key],
            f'For User Agent: "{agent_info["user_agent"][:30]}" value of parameter "{key}" doesn\'t match'
        )
