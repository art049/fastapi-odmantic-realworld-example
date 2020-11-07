from odmantic import AIOEngine

from core.exceptions import UserNotFoundException
from models.user import UserModel


async def get_user_by_username(engine: AIOEngine, username: str) -> UserModel:
    user = await engine.find_one(UserModel, UserModel.username == username)
    if user is None:
        raise UserNotFoundException()
    return user
