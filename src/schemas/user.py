from typing import Optional

from pydantic import SecretStr

from .base import BaseSchema


class LoginUser(BaseSchema):
    email: str
    password: SecretStr


class NewUser(BaseSchema):
    username: str
    email: str
    password: str


class User(BaseSchema):
    email: str
    token: str
    username: str
    bio: Optional[str] = None
    image: Optional[str] = None


class UserResponse(BaseSchema):
    user: User


class UpdateUser(BaseSchema):
    email: Optional[str] = None
    token: Optional[str] = None
    username: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[str] = None


class Profile(BaseSchema):
    username: str
    bio: Optional[str]
    image: Optional[str]
    following: bool = False


class ProfileResponse(BaseSchema):
    profile: Profile
