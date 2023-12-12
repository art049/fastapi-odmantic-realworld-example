from fastapi import APIRouter

from core.tag import get_all_tags
from schemas.tag import TagsResponse
from settings import Engine

router = APIRouter()


@router.get("/tags", response_model=TagsResponse)
async def get_tags():
    tags = await get_all_tags(Engine)
    return TagsResponse(tags=tags)
