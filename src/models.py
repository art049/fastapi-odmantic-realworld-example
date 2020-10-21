from typing import Optional

from odmantic import Model
from pydantic.types import SecretStr


class UserModel(Model):
    username: str
    email: str
    hashed_password: str
    bio: Optional[str] = None
    image: Optional[str] = None
