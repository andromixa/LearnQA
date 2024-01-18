from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("User edit tests")
class TestUserEdit(BaseCase):
    @allure.description("User create + edit test")
    def test_edit_just_created_user(self):
        # Registration
        reg_data = self.prepare_reg_data()
        response = MyRequests.post("user/", data=reg_data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = reg_data["email"]
        first_name = reg_data["firstName"]
        password = reg_data["password"]
        user_id = self.get_json_value(response, "id")

        # Login
        login_data = {"email": email, "password": password}
        response = MyRequests.post(f"user/login/", data=login_data)
        Assertions.assert_status_code(response, 200)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        # Edit
        new_first_name = "Somebody Someone"

        response = MyRequests.put(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_first_name},
        )

        Assertions.assert_status_code(response, 200)

        # Get
        response = MyRequests.get(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response, "firstName", new_first_name, f"Wrong first name after edit."
        )
