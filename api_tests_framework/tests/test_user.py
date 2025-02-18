import allure
from pydantic import BaseModel
from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @allure.title("Create new user")
    def test_create_user(self):
        self.api_users.create_user()

    @allure.title("Get user by ID")
    def test_get_user_by_id(self):
        expected_user_id = 1

        user = self.api_users.get_user_by_id(expected_user_id)
        user.user_id = expected_user_id

    @allure.title("Get all users")
    def test_get_all_users(self):
        users: BaseModel = self.api_users.get_all_users()

        assert len(users.model_dump()) > 0
