from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("User registration tests")
class TestUserRegister(BaseCase):
    @allure.description("Valid user creation test")
    def test_successful_user_create(self):
        data = self.prepare_reg_data()
        response = MyRequests.post("user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Creating user using occupied email")
    def test_create_user_with_used_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_reg_data(email)

        response = MyRequests.post("user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert (
            response.content.decode("utf-8")
            == f"Users with email '{email}' already exists"
        ), f"Unexpected response content: {response.content}"
