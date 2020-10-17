from typing import Optional, Tuple

from odmantic import Model
from odmantic.bson import ObjectId


class UserModel(Model):
    username: str
    email: str
    hashed_password: str
    bio: Optional[str] = None
    image: Optional[str] = None
    following_ids: Tuple[ObjectId, ...] = ()
