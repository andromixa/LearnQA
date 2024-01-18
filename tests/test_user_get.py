from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic('Getting user info tests')
class TestUserGet(BaseCase):
    @allure.description('Getting info for not auth user test')
    def test_get_user_not_auth(self):
        response = MyRequests.get(f"user/2")
        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_no_key(response, 'email')
        Assertions.assert_json_has_no_key(response, 'firstName')
        Assertions.assert_json_has_no_key(response, 'lastName')

    @allure.description('Getting info for current active user test')
    def test_get_user_same_as_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post(f"user/login", data=data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        user_id = self.get_json_value(response, 'user_id')

        response = MyRequests.get(
            f"user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        expected_keys = ['username', 'email', 'firstName', 'lastName']
        Assertions.assert_json_has_keys(response, expected_keys)
