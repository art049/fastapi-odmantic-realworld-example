from fastapi import APIRouter
from odmantic import AIOEngine

from core.tag import get_all_tags
from schemas.tag import TagsResponse
from settings import EngineD

router = APIRouter()


@router.get("/tags", response_model=TagsResponse)
async def get_tags(engine: AIOEngine = EngineD):
    tags = await get_all_tags(engine)
    return TagsResponse(tags=tags)
