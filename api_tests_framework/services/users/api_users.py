import allure
import requests

from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from services.users.models.user_model import UserModel, AllUsersModel

from config.headers import Headers
from utils.helper import Helper


class UserAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user,
        )

        assert response.status_code == 201, response.status_code
        self.attach_response(response.json())
        user_model = UserModel(**response.json())

        return user_model

    @allure.step("Get user by ID")
    def get_user_by_id(self, user_id):
        response = requests.get(
            url=self.endpoints.get_user_by_id(user_id),
            headers=self.headers.basic,
        )

        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        user_model = UserModel(**response.json())

        return user_model

    @allure.step("Get all users")
    def get_all_users(self):
        response = requests.get(
            url=self.endpoints.get_users_list,
            headers=self.headers.basic,
        )

        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        users_model = AllUsersModel(all_users=response.json())

        return users_model
