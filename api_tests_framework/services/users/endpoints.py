from config.env_vars import EnVariables


class Endpoints:
    create_user = f"{EnVariables.HOST}/users/"
    get_users_list = f"{EnVariables.HOST}/users/"
    get_user_by_id = lambda self, user_id: f"{EnVariables.HOST}/users/{user_id}/"
