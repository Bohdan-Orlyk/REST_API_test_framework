from fastapi import Header, HTTPException


def auth_user(token: str = Header(None)) -> None:
    if token != "MY_SUPER_SECRET_API_TOKEN":
        raise HTTPException(status_code=401, detail="Invalid or missing authentication token.")