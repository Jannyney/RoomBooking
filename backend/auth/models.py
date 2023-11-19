from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    UserID: int
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    username: str
    password: Optional[str] = None
    role: str
    can_edit: Optional[bool] = None
    can_delete: Optional[bool] = None


class Token(BaseModel):
    access_token: str
    token_type: str
    role: Optional[str] = None


class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None
