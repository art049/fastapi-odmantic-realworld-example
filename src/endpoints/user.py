from fastapi import APIRouter, Body, Depends
from odmantic import AIOEngine

from core.exceptions import InvalidCredentialsException
from models.user import UserModel
from schemas.user import LoginUser, NewUser, UpdateUser, User, UserResponse
from settings import EngineD
from utils.security import (
    OAUTH2_SCHEME,
    authenticate_user,
    create_access_token,
    get_current_user,
    get_current_user_instance,
    get_password_hash,
)

router = APIRouter()


@router.post("/users", response_model=UserResponse)
async def register_user(
    user: NewUser = Body(..., embed=True), engine: AIOEngine = EngineD
):
    instance = UserModel(
        **user.dict(), hashed_password=get_password_hash(user.password)
    )
    await engine.save(instance)
    token = create_access_token(instance)
    return UserResponse(user=User(token=token, **user.dict()))


@router.post("/users/login", response_model=UserResponse)
async def login_user(
    user_input: LoginUser = Body(..., embed=True, alias="user"),
    engine: AIOEngine = EngineD,
):
    user = await authenticate_user(
        engine, user_input.email, user_input.password.get_secret_value()
    )
    if user is None:
        raise InvalidCredentialsException()

    token = create_access_token(user)
    return UserResponse(user=User(token=token, **user.dict()))


@router.get("/user", response_model=UserResponse)
async def current_user(
    current_user: User = Depends(get_current_user),
):
    return UserResponse(user=current_user)


@router.put("/user", response_model=UserResponse)
async def update_user(
    update_user: UpdateUser = Body(..., embed=True, alias="user"),
    user_instance: User = Depends(get_current_user_instance),
    token: str = Depends(OAUTH2_SCHEME),
    engine: AIOEngine = EngineD,
):
    patch_dict = update_user.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(user_instance, name, value)
    await engine.save(user_instance)
    return UserResponse(user=User(token=token, **user_instance.dict()))
