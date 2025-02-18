from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str
    nickname: str
    user_id: int


class UserRead(User):
    pass


class UserCreate(User):
    password: str
