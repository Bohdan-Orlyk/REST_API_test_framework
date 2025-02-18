

class InnerDatabase:
    def __init__(self):
        self._USERS: dict[int, dict] = {
            233: {
                "email": "B",
                "name": "O",
                "password": "zxc123",
                "nickname": "BO",
                "user_id": 233
                },
            1: {
                "email": "S",
                "name": "H",
                "password": "zxc321",
                "nickname": "SH",
                "user_id": 1
                },
            2: {
                "email": "R",
                "name": "K",
                "password": "zxc231",
                "nickname": "RK",
                "user_id": 2
                }
        }

    def add_user(self, user: dict) -> dict | None:
        if not isinstance(user, dict):
            raise ValueError("User should have dict type")

        user_id = user.get("user_id")
        if not isinstance(user_id, int):
            raise ValueError("User must have an integer 'user_id'")

        if user_id in self._USERS:
            return user

        self._USERS[user_id] = user

        return user

    def get_all_users(self) -> list[dict]:
        return list(self._USERS.values())

    def get_user_by_id(self, user_id: int) -> dict | None:
        if not isinstance(user_id, int):
            return None

        return self._USERS.get(user_id)


db_instance = InnerDatabase()


def get_db() -> InnerDatabase:
    return db_instance
