from typing import List

from odmantic import AIOEngine

from models.article import ArticleModel


async def get_all_tags(engine: AIOEngine) -> List[str]:
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
        tags: List[str] = result[0]["all_tags"]
    else:
        tags = []
    return tags
