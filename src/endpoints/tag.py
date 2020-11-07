from fastapi import APIRouter
from odmantic import AIOEngine

from models.article import ArticleModel
from schemas.tag import TagsResponse
from settings import EngineD

router = APIRouter()


@router.get("/tags", response_model=TagsResponse)
async def get_tags(engine: AIOEngine = EngineD):
    pipeline = [
        {
            "$unwind": {
                "path": ++ArticleModel.tag_list,
                "preserveNullAndEmptyArrays": True,
            }
        },
        {
            "$group": {
                "_id": "all",
                "all_tags": {"$addToSet": ++ArticleModel.tag_list},
            }
        },
    ]
    col = engine.get_collection(ArticleModel)
    result = await col.aggregate(pipeline).to_list(length=1)
    if len(result) > 0:
        tags = result[0]["all_tags"]
    else:
        tags = []

    return TagsResponse(tags=tags)
