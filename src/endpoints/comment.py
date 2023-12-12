from fastapi import APIRouter, Body, Depends
from odmantic.bson import ObjectId

from core.article import get_article_by_slug
from core.comment import (
    add_new_comment,
    delete_comment_by_index,
    ensure_is_comment_author,
    get_article_comments_and_authors_by_slug,
    get_comment_and_index_from_id,
)
from models.article import CommentModel
from models.user import UserModel
from schemas.comment import MultipleCommentsResponse, NewComment, SingleCommentResponse
from schemas.user import User
from settings import Engine
from utils.security import get_current_user_instance

router = APIRouter()


@router.get("/articles/{slug}/comments", response_model=MultipleCommentsResponse)
async def get_article_comments(
    slug: str,
):
    data = await get_article_comments_and_authors_by_slug(Engine, slug)
    return MultipleCommentsResponse.from_comments_and_authors(data)


@router.post("/articles/{slug}/comments", response_model=SingleCommentResponse)
async def add_article_comment(
    slug: str,
    new_comment: NewComment = Body(..., embed=True, alias="comment"),
    user_instance: UserModel = Depends(get_current_user_instance),
):
    article = await get_article_by_slug(Engine, slug)
    comment_instance = CommentModel(
        authorId=user_instance.id, **new_comment.model_dump()
    )
    await add_new_comment(Engine, article, comment_instance)
    return SingleCommentResponse(
        comment={**comment_instance.dict(), "author": user_instance}
    )


@router.delete("/articles/{slug}/comments/{id}")
async def delete_article_comment(
    slug: str,
    id: ObjectId,
    user_instance: User = Depends(get_current_user_instance),
):
    article = await get_article_by_slug(Engine, slug)
    comment, index = get_comment_and_index_from_id(article, id)
    ensure_is_comment_author(user_instance, comment)
    await delete_comment_by_index(Engine, article, index)
