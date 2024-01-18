import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Authorisation tests")
class TestUserAuth(BaseCase):
    conditions = ["positive", "no_cookie", "no_token"]

    def setup_method(self):
        data = {"email": "vinkotov@example.com", "password": "1234"}

        response = MyRequests.post(f"user/login/", data=data)

        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")
        self.user_id = self.get_json_value(response, "user_id")

    @allure.description(
        "Parametrized auth tests: valid, without headers, without cookies"
    )
    @pytest.mark.parametrize("condition", conditions)
    def test_auth_user(self, condition):
        response = MyRequests.get(
            f"user/auth",
            headers={"x-csrf-token": self.token} if condition != "no_token" else None,
            cookies={"auth_sid": self.auth_sid} if condition != "no_cookie" else None,
        )

        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            0 if condition in ["no_cookie", "no_token"] else self.user_id,
            "user_id field missmatch",
        )
