from typing import Optional

from pydantic import BaseModel, SecretStr


class LoginUser(BaseModel):
    email: str
    password: SecretStr


class NewUser(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    email: str
    token: str
    username: str
    bio: Optional[str]
    image: Optional[str]


class UserResponse(BaseModel):
    user: User


class UpdateUser(BaseModel):
    email: Optional[str] = None
    token: Optional[str] = None
    username: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[str] = None


class Profile(BaseModel):
    username: str
    bio: str
    image: str
    following: bool
