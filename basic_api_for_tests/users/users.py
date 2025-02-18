from fastapi import APIRouter, Depends, HTTPException, status
from .models import UserRead, UserCreate
from services.auth_service import auth_user
from services.db_service import get_db, InnerDatabase

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(auth: None = Depends(auth_user), db: InnerDatabase = Depends(get_db)):
    all_users: list = db.get_all_users()

    return all_users


@users_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRead)
def create_user(user: UserCreate = UserCreate, auth: None = Depends(auth_user), db: InnerDatabase = Depends(get_db)):
    user = db.add_user(user.model_dump())

    return user


@users_router.get("/{user_id}/", status_code=status.HTTP_200_OK, response_model=UserRead)
def get_user_by_id(user_id: int, auth: None = Depends(auth_user), db: InnerDatabase = Depends(get_db)):
    user = db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No user with ID: {user_id}.")

    return user
