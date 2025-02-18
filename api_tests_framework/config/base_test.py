from services.users.api_users import UserAPI


class BaseTest:

    def setup_method(self):
        self.api_users = UserAPI()
        