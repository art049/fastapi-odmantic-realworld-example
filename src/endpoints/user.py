from fastapi import APIRouter, Body, Depends, status
from fastapi.exceptions import HTTPException
from odmantic import AIOEngine

from models import UserModel
from schemas.user import LoginUser, NewUser, UpdateUser, User, UserResponse
from settings import EngineD
from utils.security import (
    OAUTH2_SCHEME,
    authenticate_user,
    create_access_token,
    get_current_user,
    get_password_hash,
    get_user_instance,
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
    token = create_access_token(user)
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
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

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
    current_user: User = Depends(get_current_user),
    engine: AIOEngine = EngineD,
):
    user_instance = await get_user_instance(engine, email=current_user.email)
    patch_dict = update_user.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(user_instance, name, value)
    await engine.save(user_instance)
    return UserResponse(user=User(token=current_user.token, **user_instance.dict()))
