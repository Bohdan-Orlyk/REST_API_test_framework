from typing import List

from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    user_id: int

    @field_validator("email", "name", "nickname", "user_id")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value


class AllUsersModel(BaseModel):
    all_users: List[UserModel]
